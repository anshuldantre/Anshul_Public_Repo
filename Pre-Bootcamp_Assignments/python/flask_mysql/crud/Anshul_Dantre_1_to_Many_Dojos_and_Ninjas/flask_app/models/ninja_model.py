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
    
    @classmethod
    def delete(cls, id):
        query= "DELETE FROM ninjas WHERE id = %(id)s"
        data= {"id":id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def edit_ninja(cls, id):
        ninja = []
        query= "SELECT * FROM ninjas WHERE id = %(id)s"
        data = {"id": id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = """ UPDATE ninjas 
                    SET first_name = %(fname)s,
                        last_name = %(lname)s,
                        age = %(age)s
                    WHERE id = %(id)s"""
        data = {"id": data['id'], "fname": data['fname'], "lname": data['lname'], "age": data['age']}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results