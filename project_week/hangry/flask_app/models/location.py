
from flask_app.config.mysqlconnection import connectToMySQL

class Location:
    db_name = "hangry_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.street = data['street']
        self.city = data['city']
        self.zipcode = data['zipcode']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def add_location(cls, data):
        query = """INSERT INTO locations (name, street, city, zipcode, created_at, updated_at, user_id)
                VALUES (%(name)s, %(street)s, %(city)s, %(zipcode)s, NOW(), NOW(), %(user_id)s);"""
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_locations(cls, data):
        query = """SELECT * FROM locations
                LEFT JOIN users ON locations.user_id = users.id
                WHERE users_id = %(id)s;"""
        results = connectToMySQL(cls.db_name).query_db(query, data)
        locations = []
        if results:
            for row in results:
                locations.append( cls(row) )
        return locations

    @staticmethod
    def is_valid_location_entry(location):
        pass