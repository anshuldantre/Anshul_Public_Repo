from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route("/ninja")
def add_ninja():
    # print("within ninja_controller for add_ninja")
    return render_template("add_ninja.html", dojos=Dojo.get_all_dojos())

@app.route("/save_ninja", methods=["POST"])
def save_ninja():
    # print(f'Print the save ninja form values {request.form}')
    Ninja.add_new_ninja(request.form)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
    results = Ninja.edit_ninja(id)
    print(results)
    return render_template("edit_ninja.html", ninja = results)

@app.route("/delete_ninja/<int:id>")
def delete_ninja(id):
    Ninja.delete(id)
    ninja_list = Dojo.show_ninja(id)
    return render_template("show_ninjas.html", ninja_list = ninja_list)

@app.route("/update_ninja", methods=["POST"])
def update_ninja():
    results = Ninja.update(request.form)
    return redirect("/")