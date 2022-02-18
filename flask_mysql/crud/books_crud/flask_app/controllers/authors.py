
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author

@app.route('/')
@app.route('/authors')
def disp_default():
    return render_template('index.html', all_authors = Author.get_all_authors())

@app.route('/authors/new', methods=['POST'])
def create_author():
    Author.create_new_author(request.form)
    return redirect('/authors')