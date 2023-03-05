from Flask_App import app
from flask import Flask, render_template, session, request, redirect
from Flask_App.Model.author_model import Author

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def authors_index():
    authors = Author.list_authors()
    return render_template("author_index.html", authors_list = authors)

@app.route("/create_author", methods=["POST"])
def create_author():
    # print("within create_author controller")
    print(request.form)
    Author.insert_author(request.form)
    return redirect("/authors")