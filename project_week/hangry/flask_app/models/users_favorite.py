
from flask_app.config.mysqlconnection import connectToMySQL

class Users_favorite:
    db_name = "hangry_schema"
    def __init__(self, data):
        self.id = data('id')
        self.user_id = data('user_id')
        self.restaurant_id = data('restaurant_id')
        self.location_id = data['location_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_users_favorite(cls, data):
        query = """INSERT INTO users_favorites (user_id, restaurant_id, location_id, street, city, zipcode, created_at, updated_at)
                VALUES (%(user_id)s, %(restaurant_id)s, %(location_id)s, %(street)s, %(city)s, %(zipcode)s, NOW(), NOW());"""
        return connectToMySQL(cls.db_name).query_db(query, data)