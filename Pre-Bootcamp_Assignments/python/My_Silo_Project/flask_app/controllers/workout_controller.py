from flask_app import app
from flask_app.models.user_model import User
from flask import session, request, render_template, flash, redirect

@app.route("/workout")
def workout():
    if 'logged_in_user_id' not in session:
        flash("Session timed-out, Please login Again !","login")
        return redirect("/")
    logged_in_user = User.get_user_by_id(session['logged_in_user_id'])
    # print(logged_in_user.first_name)
    # results = Recipe.get_all_recipes()
    # , recipes = Recipe.get_all_recipes()
    return render_template("workout.html", first_name = logged_in_user.first_name)