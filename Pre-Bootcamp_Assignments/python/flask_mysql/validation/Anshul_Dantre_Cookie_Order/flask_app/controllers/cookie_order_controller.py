from flask_app import app
from flask import Flask, flash, render_template, request, session, redirect
from flask_app.models.cookie_order_model import CookieOrder

@app.route("/")
def index():
    return redirect("/cookies")

@app.route("/cookies")
def list_orders():
    return render_template("/all_orders.html", orders = CookieOrder.all_orders())

@app.route("/coookies/new")
def take_order():
    return render_template("place_order.html")

@app.route("/save", methods=['POST'])
def save_order():
    if not CookieOrder.validate_order(request.form):
        return redirect("/coookies/new")
    CookieOrder.save(request.form)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit_order(id):
    detail = CookieOrder.one_order(id)
    return render_template("/edit_order.html", detail = detail)

@app.route("/amend", methods=['POST'])
def amend_order():
    if not CookieOrder.validate_order(request.form):
        return redirect(f"/edit/{request.form['id']}")
    CookieOrder.update_order(request.form)
    return redirect("/")
