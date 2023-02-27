from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_new_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) values ( %(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW(), NOW() )"
        data = {
                "fname" :  data['fname'],
                "lname": data['lname'],
                "age" : data['age'],
                "dojo_id" : data['dojo_id']
                }
        return connectToMySQL(cls.DB).query_db(query, data)