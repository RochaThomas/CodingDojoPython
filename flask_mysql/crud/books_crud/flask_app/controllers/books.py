
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def disp_books():
    return render_template('books.html', all_books = Book.get_all_books())

@app.route('/books/<int:book_id>')
def disp_one_book(book_id):
    data = {
        'id': book_id
    }
    return render_template('book_show.html', book = Book.get_favoriting_authors(data), unfav_by = Author.not_favorited_by(data))

@app.route('/books/new', methods=['POST'])
def create_book():
    Book.create_new_book(request.form)
    return redirect('/books')

@app.route('/books/<int:book_id>/new_fav', methods=['POST'])
def fav_by_new_author(book_id):
    data = {
        'book_id': book_id,
        'author_id': request.form['author_id']
    }
    Author.set_favorite(data)
    return redirect(f"/books/{book_id}")
