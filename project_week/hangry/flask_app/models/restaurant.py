
from flask_app.config.mysqlconnection import connectToMySQL

class Restaurant:
    db_name = "hangry_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.street = data['street']
        self.city = data['city']
        self.zipcode = data['zipcode']
        self.min_away = data['min_away']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_restaurant(cls, data):
        query = "SELECT * FROM restaurants WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
