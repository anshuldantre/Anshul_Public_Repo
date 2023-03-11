from flask_app.config.mysqlconnection import connectToMySQL

class Customer:
    db="cookies_and_orders"
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_customer(cls, username):
        query = "INSERT INTO customers (username) VALUES ( %(username)s )"
        data = {"username": username}
        results = connectToMySQL(cls.db).query_db(query, data)

