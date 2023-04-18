from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Business:
    db = 'solo_project_b'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.business_name = data['business_name']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_biz(cls,data):
        query = "INSERT INTO businesses ( first_name, last_name, email, business_name, address, city, state, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(business_name)s, %(address)s, %(city)s, %(state)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(Business.db).query_db(query,data)
    
    @classmethod
    def get_biz(cls,data):
        query = "SELECT * FROM businesses WHERE id = %(id)s;"
        results = connectToMySQL(Business.db).query_db(query,data)
        return cls(results[0])
        