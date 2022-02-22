
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        return connectToMySQL('private_wall_schema').query_db(query, data)

    @classmethod
    def get_all_users(cls):
        query = """SELECT * FROM users
                ORDER BY users.first_name;"""
        results = connectToMySQL('private_wall_schema').query_db(query)
        users = []
        if results:
            for row in results:
                users.append( cls(row) )
        return users

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('private_wall_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls( result[0] )

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('private_wall_schema').query_db(query, data)
        if len(result) < 1:
            return False
        return cls( result[0] )

    @staticmethod
    def registration_is_valid(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('private_wall_schema').query_db(query, user)
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters long')
            is_valid = False
        if not user['first_name'].isalpha():
            flash('First name must contain only letters')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters long')
            is_valid = False
        if not user['last_name'].isalpha():
            flash('Last name must contain only letters')
            is_valid = False
        if len(results) >= 1:
            flash('Email is already in use')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters long')
            is_valid = False
        if user['password'].islower():
            flash('Password must contain an uppercase letter')
            is_valid = False
        num_of_nums = 0
        for char in user['password']:
            if char.isdigit():
                num_of_nums += 1
        if num_of_nums < 1:
            flash('Password must contain at least 1 number')
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash('Password and password confirmation do not match')
            is_valid = False
        return is_valid