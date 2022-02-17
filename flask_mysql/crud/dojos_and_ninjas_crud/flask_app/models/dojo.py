

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for row in results:
            dojos.append( cls(row) )

        return dojos
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            dojo.ninjas.append(Ninja(row))

        return dojo

    @classmethod
    def create_new_dojo(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());"""
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
