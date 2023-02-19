# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Friend:
    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class method to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM friends;'
        # make sure to call the ConnectToMySQL function with the schema you are targeting
        results = connectToMySQL ('First_Flask').query_db(query)
        # create an empty list to append our instance of friends
        friends = []
        # iterate over the db results and create instance of friends with cls
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def get_one(cls, id):
        print("reached friend.py")
        query = "SELECT * FROM friends where id = %(id)s"
        data = {"id" : id }
        results = connectToMySQL("first_flask").query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(occ)s, now(), now() )"
        return connectToMySQL('first_flask').query_db(query, data)
