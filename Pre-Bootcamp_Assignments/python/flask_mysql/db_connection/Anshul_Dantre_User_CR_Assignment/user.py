from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        users = []
        query = "SELECT * FROM users"
        results = connectToMySQL('user_schema').query_db(query)
        for rows in results:
            users.append( cls(rows) )
        return users
    
    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s,%(email)s, NOW(), NOW() )"
        return connectToMySQL('user_schema').query_db(query, data)