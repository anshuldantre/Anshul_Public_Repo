from flask import Flask, render_template, redirect, session, request
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
    # call the get all classmethod to get all the friends
    friends = Friend.get_all()
    # print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def create_friend():
    data = {
        "fname" : {request.form["fname"]},
        "lname" : {request.form["lname"]},
        "occ" : {request.form["occ"]}
    }
    Friend.save(data)
    return redirect('/')

@app.route("/friend/<int:id>")
def get_friend(id):
    print("reached server.py")
    friend_detail = Friend.get_one(id)
    return render_template("Friend_Detail.html", friend_detail = friend_detail)

if __name__ == '__main__':
    app.run(debug=True)