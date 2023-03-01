from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojo_list = all_dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    Dojo.create_new_dojo(request.form['dname'])
    return redirect("/dojos")

@app.route("/show_ninja/<int:id>")
def show_ninja(id):
    ninja_list = Dojo.show_ninja(id)
    # print(ninja_list.ninjas[0]['first_name'])
    return render_template("show_ninjas.html", ninja_list = ninja_list)

@app.route("/delete_dojo/<int:id>")
def delete_dojo(id):
    print(f"within controller {id}")
    result = Dojo.deletedojo(id)
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojo_list = all_dojos)

