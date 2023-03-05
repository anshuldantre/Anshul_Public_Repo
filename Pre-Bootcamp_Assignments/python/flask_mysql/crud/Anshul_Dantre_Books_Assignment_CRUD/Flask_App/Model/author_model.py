from Flask_App.Config.mysqlconnection import connectToMySQL

class Author:
    db = "books_authors_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def list_authors(cls):
        authors = []
        print("Within list_authors")
        query="SELECT * FROM authors ORDER BY name"
        results = connectToMySQL(cls.db).query_db(query)
        for rows in results:
            authors.append( cls(rows) )
        return authors
    
    @classmethod
    def insert_author(cls, data):
        print(data)
        query="INSERT INTO authors (name) VALUES ( %(aname)s )"
        data = {"aname": data['aname']}
        results = connectToMySQL(cls.db).query_db(query, data)
        return results