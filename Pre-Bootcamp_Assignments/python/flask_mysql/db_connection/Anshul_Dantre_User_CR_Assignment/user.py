from mysqlconnection import connectToMySQL

class User:
    DB = "user_schema"
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
        results = connectToMySQL(cls.DB).query_db(query)
        for rows in results:
            users.append( cls(rows) )
        return users

    @classmethod
    def show_user(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s"
        data = {"id": id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        user = []
        for all in result:
            user.append(cls(all))
        return user

    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s,%(email)s, NOW(), NOW() )"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update_user(cls, data):
        query = """UPDATE users 
                    SET first_name = %(fname)s,
                        last_name = %(lname)s,
                        email = %(email)s
                    WHERE id = %(id)s
                    """
        data = {"id": data['id'], "fname" : data['fname'], "lname": data['lname'], "email": data['email']}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        data = {"id" : data}
        return connectToMySQL(cls.DB).query_db(query, data)