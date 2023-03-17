from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users_model import User
from pprint import pprint
from flask import flash

class Posts:
    db="coding_dojo_wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod
    def validate_post(posts):
        is_valid= True
        print(posts)
        if len(posts['content'].strip()) <= 0 :
            is_valid=False
            flash("Content (Post or Comment) cannot be blank")
        return is_valid

    @classmethod
    def save_post(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES ( %(content)s, %(user_id)s )"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_posts (cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER by posts.created_at desc"
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []

        # itertae over raw data list of post dictionaries within results
            # each loop
            # --make post instance with a user object
            # --make user instance
            # --associate the user instance with the post instance
            # add post to all posts list

        for rows in results:
            # Create a post class instance from the information from each db row
            # pprint(rows, sort_dicts=False)
            one_post = cls( rows )
            # Prepare to make a user class instance, looking at the class in models/user_model.py
            one_post_user_info = {
                "id": rows['users.id'],
                "first_name" : rows['first_name'],
                "last_name" : rows['last_name'],
                "email" : rows["email"],
                "password" : rows["password"],
                "created_at" : rows["users.created_at"],
                "updated_at" : rows["users.updated_at"]
            }
            # Create the user class instance that's in the user_model.py file
            poster = User(one_post_user_info)
            # associate the post class instance with the user class instance by filling in the empty poster attribute in the post class
            one_post.user = poster
            # append the post containing the associated user to your list of posts
            all_posts.append( one_post )
        return all_posts
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM POSTS WHERE id = %(id)s"
        data = {"id": id}
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def save_comment(cls, data):
        query = "INSERT INTO comments (comment, users_id, posts_id) VALUES ( %(content)s, %(user_id)s, %(post_id)s )"
        return connectToMySQL(cls.db).query_db(query, data)
