from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.routine_model import Routine
from flask import session, request, render_template, flash, redirect

@app.route("/routine")
def routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {"user_id": session['logged_in_user_id']}
    results = Routine.get_user_routines(data)
    return render_template("routine.html", routines = results)

@app.route("/add_routine")
def add_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    return render_template("add_routine.html")

@app.route("/add_user_routine", methods=['POST'])
def add_user_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {"time": request.form['time'],
        "monday": request.form['monday'],
        "tuesday": request.form['tuesday'],
        "wednesday": request.form['wednesday'],
        "thursday": request.form['thursday'],
        "friday": request.form['friday'],
        "saturday": request.form['saturday'],
        "sunday": request.form['sunday'],
        "user_id": session['logged_in_user_id']
        }
    if not Routine.validate_routine(data):
        return redirect("/add_routine")
    results = Routine.add_new_routine(data)
    return redirect("/routine")

@app.route("/edit_routine/<int:id>")
def edit_routine(id):
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {"id": id}
    results = Routine.get_routine(data)
    return render_template("edit_routine.html", routine = results)

@app.route("/edit_user_routine", methods=['POST'])
def edit_user_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {    "time": request.form['time'],
                "monday": request.form['monday'],
                "tuesday": request.form['tuesday'],
                "wednesday": request.form['wednesday'],
                "thursday": request.form['thursday'],
                "friday": request.form['friday'],
                "saturday": request.form['saturday'],
                "sunday": request.form['sunday'],
                "id": request.form['id']
            }
    if not Routine.validate_routine(data):
        return redirect(f"/edit_routine/{request.form['id']}")
    results = Routine.edit_user_routine(data)
    return redirect("/routine")

@app.route("/delete_routine/<int:id>")
def delete_routine(id):
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    data = {"id": id}
    Routine.del_routine(data)
    return redirect("/routine")