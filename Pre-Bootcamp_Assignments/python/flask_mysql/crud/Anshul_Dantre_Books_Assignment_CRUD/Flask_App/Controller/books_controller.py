from Flask_App import app
from flask import Flask, render_template, redirect, session, request
from Flask_App.Model.book_model import Book

@app.route("/books")
def book_index():
    books = Book.get_all_books()
    return render_template("book_index.html", all_books = books)

@app.route("/add_book", methods=["POST"])
def add_book():
    # print(request.form)
    Book.add_new_book(request.form)
    return redirect("/books")