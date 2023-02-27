from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route("/add_ninja")
def add_ninja():
    # print("within ninja_controller for add_ninja")
    return render_template("add_ninja.html", dojos=Dojo.get_all_dojos())

@app.route("/save_ninja", methods=["POST"])
def save_ninja():
    # print(f'Print the save ninja form values {request.form}')
    Ninja.add_new_ninja(request.form)
    return redirect("/")