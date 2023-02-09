from mysqlconnection import connectToMySQL

# db = "bank_app"

class Bank:
    db = "bank_app"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.address = data['address']
        self.phone = data['phone']
        self.created_at = data['created_at']
        self.udpated_at = data['udpated_at']

    @classmethod
    def save(cls, data):
        query = "Insert into bank (name, address, phone) values (%(name)s,%(address)s,%(phone)s)"
        # return connectToMySQL(db,)
        return connectToMySQL(cls.db).query_db(query,data)