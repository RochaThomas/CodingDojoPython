
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.book import Book

@app.route('/books')
def disp_books():
    return render_template('books.html', all_books = Book.get_all_books())

@app.route('/books/new', methods=['POST'])
def create_book():
    Book.create_new_book(request.form)
    return redirect('/books')
