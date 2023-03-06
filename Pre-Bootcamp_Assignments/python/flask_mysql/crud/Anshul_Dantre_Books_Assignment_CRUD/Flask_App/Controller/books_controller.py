from Flask_App import app
from flask import Flask, render_template, redirect, session, request
from Flask_App.Model.book_model import Book
from Flask_App.Model.author_model import Author

@app.route("/books")
def book_index():
    books = Book.get_all_books()
    return render_template("book_index.html", all_books = books)

@app.route("/add_book", methods=["POST"])
def add_book():
    # print(request.form)
    Book.add_new_book(request.form)
    return redirect("/books")

@app.route("/books/<int:id>")
def show_book(id):
    book_details = Book.get_book_details(id)
    auth_list = Author.unfavoutire_authors(id)
    return render_template("show_book.html", book_info = book_details, auth_list = auth_list)

@app.route("/add_author_fav", methods=["POST"])
def add_new_fav():
    # print(f" Details are {request.form}")
    Book.add_author_as_fav(request.form)
    return redirect(f"/books/{request.form['book_id']}")