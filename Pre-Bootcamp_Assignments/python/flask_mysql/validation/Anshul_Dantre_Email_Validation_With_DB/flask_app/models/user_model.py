from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "user_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_users(cls):
        all_user_list = []
        query="SELECT * FROM users"
        results = connectToMySQL(cls.db).query_db(query)
        for rows in results:
            all_user_list.append( cls(rows) )
        return all_user_list
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name is required")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name is required")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email is required")
            is_valid = False
        if not REGEX_EMAIL.match(user['email']):
            flash("Invalid Email adddress")
            is_valid = False
        if not User.validate_email(user['email']):
            flash("Email already in Use")
            is_valid = False
        return is_valid
    
    @classmethod
    def add_user_to_db(cls, data):
        rec = {"first_name": data['first_name'],
                "last_name": data['last_name'],
                "email": data['email']}
        query = "INSERT INTO users (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )"
        results = connectToMySQL(cls.db).query_db(query, rec)
        return results

    @staticmethod
    def validate_email (email):
        is_valid=True
        email = email.upper()
        query="SELECT * FROM users WHERE upper(email) = %(email)s"
        data = {"email": email}
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) > 0:
            is_valid=False
        return is_valid