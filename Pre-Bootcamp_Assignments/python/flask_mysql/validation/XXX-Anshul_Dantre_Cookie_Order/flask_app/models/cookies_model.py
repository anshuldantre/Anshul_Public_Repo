from flask_app.config.mysqlconnection import connectToMySQL

class Cookie:
    db="cookies_and_orders"
    def __init__(self, data):
        self.id = data['id']
        self.cookie_type = data['cookie_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_cookie(cls, cookie_type):
        query = "INSERT INTO cookies (cookie_type) VALUES ( %(cookie_type)s )"
        data = {"cookie_type": cookie_type}
        return connectToMySQL(cls.db).query_db(query, data)
