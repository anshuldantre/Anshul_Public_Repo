from flask_app import app
from flask import Flask, request, redirect, render_template, session
from flask_app.models.users_model import User
from flask_app.models.posts_model import Posts
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("login_and_registration.html")

@app.route("/register_user", methods=['POST'])
def register_user():
    # print(request.form)
    if not User.validate_user(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {"first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
            }
    logged_in_user_id = User.resigter_user(data)
    session['logged_in_user_id'] = logged_in_user_id
    return redirect("/wall")

@app.route("/login_user", methods=['POST'])
def login_user():
    logged_in_user = User.validate_email(request.form['email'])
    if not logged_in_user:
        flash("Invald Email/Password !","login")
        return redirect("/")
    if not bcrypt.check_password_hash(logged_in_user.password, request.form['password']):
        flash("Invald Email/Password !","login")
        return redirect("/")
    session['logged_in_user_id'] = logged_in_user.id
    return redirect("/wall")

@app.route("/wall")
def login():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
    posts = Posts.get_all_posts()
    return render_template("wall.html", first_name = logged_in_user.first_name, posts = posts)

@app.route("/logout", methods=['POST'])
def logout():
    session.clear()
    return redirect("/")