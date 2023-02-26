from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route("/add_ninja")
def add_ninja():
    print("within ninja_controller for add_ninja")
    return render_template("add_ninja.html", dojos=Dojo.get_all_dojos())

# @app.route("/list_all_ninjas/<int:dojo_id>")
# def list_all_ninjas(dojo_id):
    # print(f'Reached list_all_ninjas in controller with {request.form}')
    # all_ninjas = Ninjas.list_all_ninjas()
    # return render_template("show_ninjas.html", all_ninjas = all_ninjas)

# @app.save_ninja("/save_ninja")
# def save_ninja():
#     return redirect("/")