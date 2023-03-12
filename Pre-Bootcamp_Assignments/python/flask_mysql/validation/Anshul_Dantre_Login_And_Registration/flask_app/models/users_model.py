from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_bcrypt import Bcrypt
import re

# bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "project_db"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) <= 0 or len(user['last_name']) <= 0 or len(user['email']) <= 0 or len(user['password']) <= 0 or len(user['confirm_password']) <= 0:
            flash("All fields are mandatory!")
            is_valid=False
        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            flash("First Name and Last Name should be more than 2 characters!")
            is_valid=False
        if not user['first_name'].isaplha() or not user['last_name'].isaplha():
            flash("First Name and Last Name should be letters only!")
            is_valid=False
        if user['password'] != user['confirm_password']:
            flash("Password and Confirm Password do not Match!")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password should be atleast 8 characters long!")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email !")
            is_valid=False
        return is_valid

    @classmethod
    def resigter_user(cls, details):
        query="INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s )"
        data = {"first_name" : details['first_name'],
                "last_name" : details['last_name'],
                "email" : details['email'],
                "password" : details['password']
            }
        results = connectToMySQL(cls.db).query_db(query, data)
        return results