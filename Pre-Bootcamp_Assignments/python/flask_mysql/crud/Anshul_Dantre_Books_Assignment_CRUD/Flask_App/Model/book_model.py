from Flask_App.Config.mysqlconnection import connectToMySQL

class Book:
    db = "books_authors_schema"
    def __init__(self, data):
        self.id = data['id']
        self.tilte = data['tilte']
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