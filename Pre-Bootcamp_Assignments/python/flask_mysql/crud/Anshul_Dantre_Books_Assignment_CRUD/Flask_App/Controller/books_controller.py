from Flask_App import app
from flask import Flask, render_template, redirect, session
from Flask_App.Model.book_model import Book

@app.route("/books")
def book_index():
    all_books = Book.get_all_books()
    return redirect("book_index.html", all_books)