from flask_app import app
from flask import Flask, render_template, session, request, redirect
from flask_app.models.user_model import User


@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def get_all():
    return render_template("users.html", all_users = User.get_all_users())

@app.route('/users/new')
def add_user():
    return render_template("add_user.html")

@app.route('/create', methods=["post"])
def add_users():
    session['user_detail'] = request.form
    # print(f'Within controller {session["user_detail"]}')
    if not User.validate_user(request.form):
        return redirect("/users/new")
    User.add_user_to_db(request.form)
    session['user_detail'] = None
    return redirect("/")