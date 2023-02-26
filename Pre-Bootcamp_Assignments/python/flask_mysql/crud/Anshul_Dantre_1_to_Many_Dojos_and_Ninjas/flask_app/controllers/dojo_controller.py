from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo

@app.route("/")
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojo_list = all_dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    print(f"reached controller with {request.form['dname']}")
    Dojo.create_new_dojo(request.form['dname'])
    return redirect("/")