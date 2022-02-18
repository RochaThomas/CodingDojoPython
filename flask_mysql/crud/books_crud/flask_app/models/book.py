
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_by_authors = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        if results:
            for row in results:
                books.append( cls(row) )
        return books

    @classmethod
    def create_new_book(cls, data):
        query = """INSERT INTO books (title, num_of_pages, created_at, updated_at)
                VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"""
        return connectToMySQL("books_schema").query_db(query, data)
    
    @classmethod
    def get_favoriting_authors(cls, data):
        query = """SELECT * FROM books
                LEFT JOIN authors_favorite_books ON authors_favorite_books.book_id = books.id
                LEFT JOIN authors ON authors_favorite_books.author_id = authors.id
                WHERE books.id = %(id)s;"""
        results = connectToMySQL('books_schema').query_db(query, data)
        if results:
            book = cls( results[0] )
            for row in results:
                author_info = {
                    'id': row['authors.id'],
                    'name': row['authors.name'],
                    'created_at': row['authors.created_at'],
                    'updated_at': row['authors.updated_at']
                }
                book.favorited_by_authors.append( author.Author( author_info ))
        return book