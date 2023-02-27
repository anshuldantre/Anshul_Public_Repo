from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo:
    DB  = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_new_dojo(cls, name):
        # print(f"recahed model with {name}")
        query = "INSERT INTO dojos (name) VALUES (%(dname)s, NOW(), NOW() )"
        data = {"dname": name}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        dojo_list = []
        # print(f'reached get_all_dojos')
        query = "SELECT * FROM dojos ORDER BY name"
        results = connectToMySQL(cls.DB).query_db(query)
        for rows in results:
            dojo_list.append( cls(rows) )
        return dojo_list
    
    @classmethod
    def get_all_ninjas_in_a_dojo(cls, id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s ORDER BY ninjas.first_name"
        data = {"dojo_id" : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls( results[0] )
        for all_ninjas in results:
            # print(f"age is {all_ninjas['age']}")
            ninja_list = {
                "id": all_ninjas['ninjas.id'],
                "first_name": all_ninjas['first_name'],
                "last_name": all_ninjas['last_name'],
                "age": all_ninjas['age'],
                "dojo_id": all_ninjas['dojo_id'],
                "created_at": all_ninjas['ninjas.created_at'],
                "updated_at": all_ninjas['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(ninja_list) )
        return dojo