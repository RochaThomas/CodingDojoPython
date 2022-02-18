
from flask_app import app
from flask_app.controllers.authors import Author
from flask_app.controllers.books import Book

if __name__ == '__main__':
    app.run(debug = True)