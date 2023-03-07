from flask_app import app
from flask import Flask, render_template, session, request, redirect


@app.route("/")
def add_user():
    return render_template("add_user.html")