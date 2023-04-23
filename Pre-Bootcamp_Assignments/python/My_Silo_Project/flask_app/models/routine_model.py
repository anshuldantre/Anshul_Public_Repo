from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class Routine:
    db = "workout_recorder"
    def __init__(self, data):
        self.id = data['id']
        self.time = data['time']
        self.monday = data['monday']
        self.tuesday = data['tuesday']
        self.wednesday = data['wednesday']
        self.thursday = data['thursday']
        self.friday = data['friday']
        self.saturday = data['saturday']
        self.sunday = data['sunday']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_new_routine(cls, data):
        query = """INSERT INTO routines (time, monday, tuesday, wednesday, thursday, friday, saturday, sunday, user_id)
        VALUES ( %(time)s, %(monday)s, %(tuesday)s, %(wednesday)s, %(thursday)s, %(friday)s, %(saturday)s, %(sunday)s, %(user_id)s )"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_routines(cls, data):
        all_routines = []
        query = "SELECT * FROM routines WHERE user_id = %(user_id)s ORDER BY id"
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            all_routines.append( cls(row) )
        return all_routines

    @classmethod
    def get_routine(cls, id):
        query = "SELECT * FROM routines WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, id)
        if len(results) < 1:
            return False
        return cls( results[0] )

    @classmethod
    def edit_user_routine(cls, data):
        query = """UPDATE routines
                    SET time = %(time)s,
                        monday = %(monday)s,
                        tuesday = %(tuesday)s,
                        wednesday = %(wednesday)s,
                        thursday = %(thursday)s,
                        friday = %(friday)s,
                        saturday = %(saturday)s,
                        sunday = %(sunday)s
                    WHERE id = %(id)s"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def del_routine(cls, id):
        query = "DELETE FROM routines WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, id)
