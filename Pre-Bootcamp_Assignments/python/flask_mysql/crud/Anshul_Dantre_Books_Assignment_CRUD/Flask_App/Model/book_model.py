from Flask_App.Config.mysqlconnection import connectToMySQL
from Flask_App.Model import author_model

class Book:
    db = "books_authors_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favourited_by = []
    
    @classmethod
    def get_all_books(cls):
        book_list = []
        query = "SELECT * FROM books ORDER by title"
        results = connectToMySQL(cls.db).query_db(query)
        for rows in results:
            book_list.append( cls(rows) )
        return book_list
    
    @classmethod
    def unfavoutire_books(cls, id):
        unfav_list = []
        query="SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM favourites WHERE author_id = %(id)s)"
        data = { "id" : id }
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        for rows in results:
            unfav_list.append( cls(rows) )
        return unfav_list

    @classmethod
    def add_new_book(cls, book_details):
        # print(book_details)
        data = {
            "title" : book_details['title'],
            "num_of_pages" : book_details['num_of_pages']
        }
        query = "INSERT INTO books (title, num_of_pages) values ( %(title)s, %(num_of_pages)s )"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def get_book_details(cls, id):
        book = []
        data = { "id" : id }
        print(data)
        query = """SELECT *
                    FROM books
                    LEFT JOIN favourites
                        ON books.id = favourites.book_id
                    LEFT JOIN authors
                        ON favourites.author_id = authors.id
                    WHERE books.id = %(id)s"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        book = cls( results[0] )
        for rows in results:
            if rows['authors.id'] == None:
                break
            author_list = {
                "id" : rows['authors.id'],
                "name" : rows['name'],
                "created_at" : rows['authors.created_at'],
                "updated_at" : rows['authors.updated_at']
            }
            book.favourited_by.append( author_model.Author(author_list) )
        return book
    
    @classmethod
    def add_author_as_fav(cls, author_details):
        # print(f"author_details are {author_details}")
        data = { "author_id" : author_details['author_id'],
                "book_id" : author_details['book_id']}
        query = "INSERT INTO favourites values ( %(author_id)s, %(book_id)s )"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results