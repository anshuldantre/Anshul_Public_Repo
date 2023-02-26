from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB  = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_dojo(cls, name):
        # print(f"recahed model with {name}")
        query = "INSERT INTO dojos (name) VALUES (%(dname)s, NOW(), NOW() )"
        data = {"dname": name}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        dojo_list = []
        print(f'reached get_all_dojos')
        query = "SELECT * FROM dojos ORDER BY name"
        results = connectToMySQL(cls.DB).query_db(query)
        for rows in results:
            dojo_list.append( cls(rows) )
        return dojo_list