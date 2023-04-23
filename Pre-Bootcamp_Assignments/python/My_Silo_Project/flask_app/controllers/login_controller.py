from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register_user", methods=["POST"])
def register_user():
    print(request.form)
    if not User.validate_user(request.form):
        print("validating user")
        return redirect("/")
    print("validated")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {"first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
            }
    logged_in_user_id = User.resigter_user(data)
    session['logged_in_user_id'] = logged_in_user_id
    return redirect("/routine")

@app.route("/login_user", methods=['POST'])
def login_user():
    logged_in_user = User.validate_email(request.form['email'])
    if not logged_in_user:
        flash("Invald Email or Password !","login")
        return redirect("/")
    if not bcrypt.check_password_hash(logged_in_user.password, request.form['password']):
        flash("Invald Email or Password !","login")
        return redirect("/")
    session['logged_in_user_id'] = logged_in_user.id
    return redirect("/routine")

@app.route("/logout", methods=['POST'])
def logout():
    session.clear()
    return redirect("/")