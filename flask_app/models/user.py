from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'solo_project_b'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.birthday = data['birthday']
        self.skills = data['skills']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
  
    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users ( first_name, last_name, email, birthday, skills, address, city, state, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(birthday)s, %(skills)s, %(address)s, %(city)s, %(state)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL(User.db).query_db(query,data)
    
    @classmethod
    def update_user(cls, data):
        query = " UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,birthday=%(birthday)s,skills=%(skills)s,address=%(address)s,city=%(city)s,state=%(state)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(User.db).query_db( query, data )


    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(User.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(eml)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(eml)s;"
        results = connectToMySQL(User.db).query_db(query,user)
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
        if len(user['bday']) < 6:
            flash("Please enter birthday","register")
            is_valid = False
        if len(user['desc']) < 10:
            flash("Description should be at least 10 characters long","register")
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
        if len(user['carp']) < 1 or len(user['cem']) < 1 or len(user['dry']) < 1 or len(user['hvmc']) < 1 or len(user['high']) < 1 or len(user['home']) < 1 or len(user['hvac']) < 1 or len(user['plmg']) < 1:
            flash("Please enter all fields of experience","register")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_update(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(eml)s;"
        results = connectToMySQL(User.db).query_db(query,user)
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
        if len(user['bday']) < 6:
            flash("Please enter birthday","register")
            is_valid = False
        if len(user['desc']) < 10:
            flash("Description should be at least 10 characters long","register")
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
        if len(user['carp']) < 1 or len(user['cem']) < 1 or len(user['dry']) < 1 or len(user['hvmc']) < 1 or len(user['high']) < 1 or len(user['home']) < 1 or len(user['hvac']) < 1 or len(user['plmg']) < 1:
            flash("Please enter all fields of experience","register")
            is_valid = False
        return is_valid
    
class Trade:
    db = 'solo_project_b'
    def __init__(self,data):
        self.id = data['id']
        self.carpentry = data['carpentry']
        self.cement = data['cement']
        self.drywall = data['drywall']
        self.heavy_machinery = data['heavy_machinery']
        self.high_v_electricity = data['high_v_electricity']
        self.home_electricity = data['home_electricity']
        self.hvac = data['hvac']
        self.plumbing = data['plumbing']
        self.user_id = data['user_id']

    @classmethod
    def save_skills(cls,data):
        query = "INSERT INTO trades ( carpentry, cement, drywall, heavy_machinery, high_v_electricity, home_electricity, hvac, plumbing, user_id ) VALUE ( %(carpentry)s, %(cement)s, %(drywall)s, %(heavy_machinery)s, %(high_v_electricity)s, %(home_electricity)s, %(hvac)s, %(plumbing)s, %(user_id)s );"

        return connectToMySQL(User.db).query_db(query,data)
    
    @classmethod
    def get_skills(cls,data):
        query = "SELECT * FROM trades WHERE user_id = %(user_id)s;"
        results = connectToMySQL(User.db).query_db(query,data)
        return cls(results[0])
    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(User.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update_skills(cls, data):
        query = " UPDATE skills SET carpentry=%(carpentry)s,cement=%(cement)s,drywall=%(drywall)s,heavy_machinery=%(heavy_machinery)s,high_v_electricity=%(high_v_electricity)s,home_elecricity=%(home_elecricity)s,hvac=%(hvac)s,plumbing=%(plumbing)s,updated_at=NOW() WHERE user_id = %(user_id)s;"
        return connectToMySQL(User.db).query_db( query, data )