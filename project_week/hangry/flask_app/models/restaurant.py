
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

    @classmethod
    def get_all_favorites_for_user(cls, data):
        query = """SELECT * FROM users
                LEFT JOIN users_favorites ON users.id = users_favorites.user_id
                LEFT JOIN restaurants ON users_favorites.restaurant_id = restaurants.id
                WHERE users.id = %(id)s;"""
        results = connectToMySQL(cls.db_name).query_db(query, data)
        users_favorites = []
        if results:
            for row in results:
                users_favorites.append( cls(row) )
        return users_favorites


    @classmethod
    def get_all_favorites_for_location(cls, data):
        query = """SELECT * FROM locations
                LEFT JOIN users_favorites ON locations.id = users_favorites.location_id
                LEFT JOIN restaurants ON users_favorites.restaurant_id = restaurants.id
                WHERE locations.id = %(id)s;"""
        results = connectToMySQL(cls.db_name).query_db(query, data)
        favorites_for_location = []
        if results:
            for row in results:
                favorites_for_location.append( cls(row) )
        return favorites_for_location

    @classmethod
    def get_one_random(cls, data):
        pass

    @staticmethod
    def is_valid_restaurant_entry(restaurant):
        pass