
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("books_schema").query_db(query)
        authors = []
        if results:
            for row in results:
                authors.append( cls(row) )
        return authors

    @classmethod
    def create_new_author(cls, data):
        query = """INSERT INTO authors (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());"""
        return connectToMySQL("books_schema").query_db(query, data)

    @classmethod
    def set_favorite(cls, data):
        query = """INSERT INTO authors_favorite_books (book_id, author_id)
                VALUES (%(book_id)s, %(author_id)s);"""
        return connectToMySQL("books_schema").query_db(query, data)

    @classmethod
    def not_favorited_by(cls, data):
        query = """SELECT * FROM authors
                WHERE authors.id
                NOT IN (SELECT author_id FROM authors_favorite_books
                WHERE book_id = %(id)s);"""
        authors = []
        results = connectToMySQL("books_schema").query_db(query, data)
        if results:
            for row in results:
                authors.append( cls(row) )
        return authors

    @classmethod
    def get_authors_favorites(cls, data):
        query = """SELECT * FROM authors
                LEFT JOIN authors_favorite_books ON authors.id = authors_favorite_books.author_id
                LEFT JOIN books ON books.id = authors_favorite_books.book_id
                WHERE authors.id = %(id)s;"""
        results = connectToMySQL("books_schema").query_db(query, data)
        author = cls(results[0])
        if results:
            for row in results:
                book_data = {
                    "id": row['books.id'],
                    "title": row['title'],
                    "num_of_pages": row['num_of_pages'],
                    "created_at": row['books.created_at'],
                    "updated_at": row['books.updated_at']
                }
                author.fav_books.append( book.Book(book_data) )
        return author