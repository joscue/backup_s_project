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
                                     
    @classmethod
    def bget_by_email(cls,data):
        query = "SELECT * FROM businesses WHERE email = %(eml)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def update_biz(cls, data):
        query = " UPDATE businesses SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,business_name=%(business_name)s,address=%(address)s,city=%(city)s,state=%(state)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(Business.db).query_db( query, data )
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(eml)s;"
        results = connectToMySQL(Business.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['eml']):
            flash("Invalid Email","register")
            is_valid = False
        if len(user['fname']) < 3:
            flash("First name must be at least 2 characters","register")
            is_valid = False
        if len(user['lname']) < 3:
            flash("Last name must be at least 2 characters","register")
            is_valid = False
        if len(user['bname']) < 3:
            flash("Business name must be 3 characters", "register")
            is_valid = False
        if len(user['adrs']) < 8:
            flash("Address must be at least 8 characters","register")
            is_valid = False
        if len(user['city']) < 4:
            flash("City must be at least 4 characters","register")
            is_valid = False
        if len(user['st']) != 2:
            flash("State must be 2 characters","register")
            is_valid = False
        if len(user['pswd']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid = False
        if user['pswd'] != user['con']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid
    @staticmethod
    def validate_update(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(eml)s;"
        results = connectToMySQL(Business.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['eml']):
            flash("Invalid Email","register")
            is_valid = False
        if len(user['fname']) < 3:
            flash("First name must be at least 2 characters","register")
            is_valid = False
        if len(user['lname']) < 3:
            flash("Last name must be at least 2 characters","register")
            is_valid = False
        if len(user['bname']) < 3:
            flash("Business name must be at least 3 characters","register")
            is_valid = False
        if len(user['adrs']) < 8:
            flash("Address must be at least 8 characters","register")
            is_valid = False
        if len(user['city']) < 4:
            flash("City must be at least 4 characters","register")
            is_valid = False
        if len(user['st']) != 2:
            flash("State must be 2 characters","register")
            is_valid = False
        return is_valid