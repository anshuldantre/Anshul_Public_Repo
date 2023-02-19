from flask import Flask, render_template, redirect, session, request
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("index.html", all_users = users)

@app.route("/show_user/<int:id>")
def show_user(id):
    result = User.show_user(id)
    return render_template("show_user.html", user_detail = result)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    User.add_new_user(request.form)
    return redirect("/")

@app.route("/update/<int:id>")
def update(id):
    result = User.show_user(id)
    return render_template("update_user.html", user_detail = result)

@app.route("/update_user", methods=["POST"])
def update_user():
    print(request.form)
    User.update_user(request.form)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    print("within delete")
    User.delete_user(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)