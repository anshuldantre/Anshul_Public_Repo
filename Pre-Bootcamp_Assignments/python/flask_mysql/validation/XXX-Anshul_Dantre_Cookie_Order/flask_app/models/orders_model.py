from flask_app.config.mysqlconnection import connectToMySQL

class Orders:
    db = "cookies_and_orders"
    def __init__(self, data):
        self.cookie_id = data['cookie_id']
        self.customer_id = data['customer_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_order(cls, order):
        query = "INSERT INTO orders (cookie_id, customer_id) VALUES ( %()s, %()s )"
        data = {"cookie_id": order["cookie_id"], "customer_id": data['customer_id'] }
        return connectToMySQL(cls.db).query_db(query, data)