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

    # Now we use class methof to query our database
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
