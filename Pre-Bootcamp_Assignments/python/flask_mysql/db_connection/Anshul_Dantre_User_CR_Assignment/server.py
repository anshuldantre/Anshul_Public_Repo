from flask import Flask, render_template, redirect, session, request
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("index.html", all_users = users)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    User.add_new_user(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
