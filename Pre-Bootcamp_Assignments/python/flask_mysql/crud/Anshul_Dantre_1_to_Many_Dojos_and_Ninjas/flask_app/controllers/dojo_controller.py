from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo

@app.route("/")
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojo_list = all_dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    Dojo.create_new_dojo(request.form['dname'])
    return redirect("/")

@app.route("/get_all_ninjas_in_dojo/<int:id>")
def get_all_ninjas_in_dojo(id):
    ninja_list = Dojo.get_all_ninjas_in_a_dojo(id)
    return render_template("show_ninjas.html", ninja_list = ninja_list)