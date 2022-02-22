
from datetime import datetime
import math
from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.sender = data['sender']
        self.receiver = data['receiver']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        # got this method from Coding Dojo learning platform
        now = datetime.now()
        change = now - self.created_at
        if change.days > 0:
            return f"{change.days} days ago"
        elif (math.floor(change.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(change.total_seconds() / 60)/60)} hours ago"
        elif change.total_seconds() >= 60:
            return f"{math.floor(change.total_seconds() / 60)} minutes ago"
        else: 
            return f"{math.floor(change.total_seconds())} seconds ago"

    @classmethod
    def get_received_messages(cls, data):
        query = """SELECT CONCAT(users.first_name, ' ', users.last_name) as sender, CONCAT(users2.first_name, ' ', users2.last_name) as receiver, messages.* 
                FROM users
                LEFT JOIN messages ON users.id = messages.sender_id
                LEFT JOIN users as users2 ON users2.id = messages.receiver_id
                WHERE users2.id = %(id)s;"""
        results = connectToMySQL('private_wall_schema').query_db(query, data)
        messages = []
        if results:
            for row in results:
                messages.append( cls(row) )
        return messages
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO messages (sender_id, receiver_id, content, created_at, updated_at)
                VALUES (%(sender_id)s, %(receiver_id)s, %(content)s, NOW(), NOW());"""
        return connectToMySQL('private_wall_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        return connectToMySQL('private_wall_schema').query_db(query, data)

    @staticmethod
    def is_valid_message(message):
        is_valid = True
        if len(message['content']) < 5:
            flash('Message must be at least 5 characters long')
            is_valid = False
        return is_valid
