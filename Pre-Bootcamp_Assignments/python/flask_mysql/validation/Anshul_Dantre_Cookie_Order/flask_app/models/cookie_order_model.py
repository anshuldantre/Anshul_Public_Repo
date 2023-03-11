from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class CookieOrder:
    db="cookieorders"
    def __init__(self, data):
        self.id = data['id']
        self.cookie_type = data['cookie_type']
        self.customer_name = data['customer_name']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, order):
        query = "INSERT INTO cookie_orders (cookie_type, customer_name, num_of_boxes) VALUES ( %(cookie_type)s, %(customer_name)s, %(num_of_boxes)s )"
        data = {"cookie_type": order['cookie_type'],
                "customer_name": order['customer_name'],
                "num_of_boxes": order['num_of_boxes']}
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def all_orders(cls):
        orders = []
        query = "SELECT * FROM cookie_orders ORDER BY id"
        results = connectToMySQL(cls.db).query_db(query)
        for rows in results:
            orders.append( cls(rows) )
        return orders

    @classmethod
    def one_order(cls, id):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s"
        id = {"id": id}
        results = connectToMySQL(cls.db).query_db(query, id)
        return results

    @classmethod
    def update_order(cls, data):
        print(f"data is {data}")
        query = """UPDATE cookie_orders
                        SET customer_name = %(customer_name)s,
                        cookie_type = %(cookie_type)s,
                        num_of_boxes = %(num_of_boxes)s
                    WHERE id = %(id)s
                """
        data = {"customer_name": data['customer_name'], 
                "cookie_type" : data['cookie_type'],
                "num_of_boxes" : data['num_of_boxes'],
                "id" : data['id']}
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @staticmethod
    def validate_order(data):
        is_valid = True
        if len(data['customer_name']) < 1:
            flash("Customer Name is required")
            is_valid=False
        if len(data['customer_name']) <= 2:
            flash("Customer Name must be more than 2 characters")
            is_valid=False
        if len(data['cookie_type']) < 1:
            flash("Cookie Type is required")
            is_valid=False
        if len(data['cookie_type']) <= 2:
            flash("Cookie Type must be more than 2 characters")
            is_valid=False
        if len(data['num_of_boxes']) <= 0:
            flash("Number of Boxes is required")
            is_valid=False
        if len(data['num_of_boxes']) > 0:
            if int(data['num_of_boxes']) <= 0:
                flash("Number of Boxes cannot be negative or zero")
                is_valid=False
        return is_valid