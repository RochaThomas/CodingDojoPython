
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
@app.route('/authors')
def disp_default():
    return render_template('index.html', all_authors = Author.get_all_authors())

@app.route('/authors/<int:author_id>')
def disp_author(author_id):
    data = {
        'id': author_id
    }
    return render_template('author_show.html', author = Author.get_authors_favorites(data), unfav_books = Book.not_favorited(data))

@app.route('/authors/new', methods=['POST'])
def create_author():
    Author.create_new_author(request.form)
    return redirect('/authors')

@app.route('/authors/<int:author_id>/new_fav', methods=['POST'])
def authors_new_fav(author_id):
    data = {
        'book_id': request.form['book_id'],
        'author_id': author_id
    }
    Author.set_favorite(data)
    return redirect(f"/authors/{author_id}")