
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name='recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        if results:
            for row in results:
                recipes.append( cls(row) )
        return recipes

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes where id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if not results:
            return False
        return cls( results[0] )

    @classmethod
    def save(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, date_made_on, under_30, created_at, updated_at, user_id)
                VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made_on)s, %(under_30)s, NOW(), NOW(), %(user_id)s);"""
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes SET 
                name = %(name)s, 
                description = %(description)s, 
                instructions = %(instructions)s, 
                date_made_on = %(date_made_on)s, 
                under_30 = %(under_30)s, 
                updated_at = NOW()
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
        

    @staticmethod
    def is_valid_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name of recipe must be at least 3 characters long", 'recipes_error')
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description of recipe must be at least 3 characters long", 'recipes_error')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions of recipe must be at least 3 characters long", 'recipes_error')
            is_valid = False
        if recipe['date_made_on'] == '' or recipe['under_30'] == '':
            flash("All criteria must be filled out", 'recipes_error')
            is_valid = False
        return is_valid