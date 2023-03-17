from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.users_model import User
from flask_app.models.posts_model import Posts

@app.route("/create_post", methods=['POST'])
def create_post():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {"content" : request.form['content'],
            "user_id" : session['logged_in_user_id']}
    if not Posts.validate_post(request.form):
        return redirect("/wall")
    results = Posts.save_post (data)
    return redirect("/wall")

@app.route("/delete/<int:id>")
def delete_post(id):
    Posts.delete(id)
    return redirect("/wall")


@app.route("/add_comment", methods=["POST"])
def add_comment():
    if not Posts.validate_post(request.form):
        return redirect("/wall")
    results = Posts.save_comment(request.form)
    return redirect("/wall")