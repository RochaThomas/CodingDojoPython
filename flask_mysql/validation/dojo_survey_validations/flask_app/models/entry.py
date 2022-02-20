
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Entry:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_entry(entry):
        is_valid = True
        if len(entry['name']) < 5:
            flash("Name must be at least 5 characters")
            is_valid = False
        if not 'location' in entry:
            flash("Select a location")
            is_valid = False
        if not 'language' in entry:
            flash("Select a language")
            is_valid = False
        if len(entry['comment']) < 1:
            flash("Add a comment")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = """INSERT INTO entries (name, location, language, comment, created_at, updated_at)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"""
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @classmethod
    def get_one_survey_info(cls, data):
        query = "SELECT * FROM entries WHERE name = %(name)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return cls( results[0] )