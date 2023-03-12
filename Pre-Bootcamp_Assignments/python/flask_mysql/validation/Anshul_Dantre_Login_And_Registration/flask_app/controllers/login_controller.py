from flask_app import app
from flask import Flask, request, redirect, render_template, session

@app.route("/")
def index():
    return render_template("login_and_registration.html")