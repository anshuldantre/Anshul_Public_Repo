from Flask_App.Config.mysqlconnection import connectToMySQL
# from Flask_App.Model.author_model import Author

class Book:
    db = "books_authors_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
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
        print(book_details)
        data = {
            "title" : book_details['title'],
            "num_of_pages" : book_details['num_of_pages']
        }
        query = "INSERT INTO books (title, num_of_pages) values ( %(title)s, %(num_of_pages)s )"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results