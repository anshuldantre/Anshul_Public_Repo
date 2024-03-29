from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from datetime import date, timedelta, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "project_db"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.dob = data['dob']
        self.gender = data['gender']
        self.music = data['music']
        self.sports = data['sports']
        self.studies = data['studies']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        allowed_dob = datetime.today() - timedelta(days=365*15)
        is_valid = True
        if len(user['first_name'].strip()) <= 0 or len(user['last_name'].strip()) <= 0 or len(user['email'].strip()) <= 0 or len(user['password'].strip()) <= 0 or len(user['confirm_password'].strip()) <= 0 or len(user['dob']) <= 0 or user.get('gender') == None or ( user.get('music') == None and user.get('sports') == None and user.get('studies') == None ):
            flash("All fields are mandatory!","register")
            is_valid=False
        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            flash("First and Last Name should be more than 2 characters!","register")
            is_valid=False
        if not ( user['first_name'].isalpha() and user['last_name'].isalpha() ):
            flash("First Name and Last Name should be letters only!","register")
            is_valid=False
        if user['password'] != user['confirm_password']:
            flash("Password and Confirm Password do not Match!","register")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password should be atleast 8 characters long!","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email !","register")
            is_valid=False
        if len(user['email']) > 0:
            logged_in_user = User.validate_email(user['email'])
            if logged_in_user:
                if logged_in_user.id > 0:
                    flash("Email already resgistered !","register")
                    is_valid=False
        if datetime.strptime(user['dob'], '%Y-%m-%d') > allowed_dob:
            flash("User should be 15 and older !","register")
            is_valid=False
        return is_valid

    @classmethod
    def validate_email(cls, email):
        lower_email = email.lower()
        query="SELECT * FROM users WHERE lower(email) = %(email)s"
        data = {"email" : lower_email}
        logged_in_user = connectToMySQL(cls.db).query_db(query, data)
        if len(logged_in_user) < 1:
            return False
        return cls( logged_in_user[0] )

    @classmethod
    def resigter_user(cls, details):
        query="INSERT INTO users (first_name, last_name, email, password, dob, gender, music, sports, studies) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, %(dob)s , %(gender)s, %(music)s, %(sports)s, %(studies)s )"
        data = {"first_name" : details['first_name'],
                "last_name" : details['last_name'],
                "email" : details['email'],
                "password" : details['password'],
                "dob" : details['dob'],
                "gender" : details['gender'],
                "music" : details['music'],
                "sports" : details['sports'],
                "studies" : details['studies']
            }
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_user_by_id(cls, id):
        query="SELECT * FROM users WHERE id = %(id)s"
        data = {"id" : id}
        logged_in_user = connectToMySQL(cls.db).query_db(query, data)
        if len(logged_in_user) < 1:
            return False
        return cls( logged_in_user[0] )