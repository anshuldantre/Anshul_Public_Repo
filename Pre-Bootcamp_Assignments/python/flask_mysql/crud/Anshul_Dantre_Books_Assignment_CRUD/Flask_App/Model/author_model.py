from Flask_App.Config.mysqlconnection import connectToMySQL
from Flask_App.Model import book_model

class Author:
    db = "books_authors_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_book = []

    @classmethod
    def list_authors(cls):
        authors = []
        # print("Within list_authors")
        query="SELECT * FROM authors ORDER BY name"
        results = connectToMySQL(cls.db).query_db(query)
        for rows in results:
            authors.append( cls(rows) )
        return authors
    
    @classmethod
    def insert_author(cls, data):
        # print(data)
        query="INSERT INTO authors (name) VALUES ( %(aname)s )"
        data = {"aname": data['aname']}
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_authors_favourite(cls, id):
        # print("Within get_authors_favourite model")
        query= """
        SELECT *
            FROM authors a 
            LEFT JOIN favourites f 
                ON a.id = f.author_id
            LEFT JOIN books b
                ON f.book_id = b.id
            WHERE a.id = %(id)s;
        """
        data = { "id" : id }
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        author = cls( results[0] )

        for rows in results:
            if rows["b.id"] == None:
                break
            fav_list = {
                "id" : rows["b.id"],
                "title" : rows["title"],
                "num_of_pages" : rows['num_of_pages'],
                "created_at" : rows['b.created_at'],
                "updated_at" : rows['b.updated_at']
            }
            author.fav_book.append( book_model.Book( fav_list))
        return author

    @classmethod
    def add_book_as_fav(cls, add_book):
        data = { "author_id" : add_book['author_id'],
                "book_id" : add_book['book_id']}
        query = "INSERT INTO favourites values ( %(author_id)s, %(book_id)s )"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results


    @classmethod
    def unfavoutire_authors(cls, id):
        unfav_list = []
        query="SELECT * FROM authors WHERE id NOT IN (SELECT author_id FROM favourites WHERE book_id = %(id)s ) ORDER BY name"
        data = { "id" : id }
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        for rows in results:
            unfav_list.append( cls(rows) )
        return unfav_list
    
 