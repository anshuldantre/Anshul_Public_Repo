from Flask_App import app
from flask import Flask, render_template, session, request, redirect
from Flask_App.Model.author_model import Author
from Flask_App.Model.book_model import Book

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
    # print(request.form)
    Author.insert_author(request.form)
    return redirect("/authors")

@app.route("/authors/<int:id>")
def show_author(id):
    # print(f"Within authors controller {id}")
    auth_fav = Author.get_authors_favourite(id)
    unfavoutire_books = Book.unfavoutire_books(id)
    return render_template("/show_author.html", favourites = auth_fav, unfavoutires = unfavoutire_books)

@app.route("/add_favourite", methods=["POST"])
def add_fav():
    # print(f"Within add_fav controller {(request.form)}")
    Author.add_book_as_fav(request.form)
    return redirect(f"/authors/{request.form['author_id']}")