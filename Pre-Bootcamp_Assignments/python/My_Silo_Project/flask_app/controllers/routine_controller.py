from flask_app import app
from flask_app.models.user_model import User
from flask import session, request, render_template, flash, redirect
from flask_app.models.routine_model import Routine

@app.route("/routine")
def routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
    data = {"user_id": session['logged_in_user_id']}
    results = Routine.get_user_routines(data)
    return render_template("routine.html", first_name = logged_in_user.first_name, routines = results)

@app.route("/add_routine")
def add_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
    return render_template("add_routine.html", first_name = logged_in_user.first_name)

@app.route("/add_user_routine", methods=['POST'])
def add_user_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
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
    results = Routine.add_new_routine(data)
    return redirect("/routine")

@app.route("/edit_routine/<int:id>")
def edit_routine(id):
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
    data = {"id": id}
    results = Routine.get_routine(data)
    print("after get_routine",results.time)
    return render_template("edit_routine.html", first_name = logged_in_user.first_name, routine = results)

@app.route("/edit_user_routine", methods=['POST'])
def edit_user_routine():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
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