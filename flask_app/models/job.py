from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, business

class Job:
    db = 'solo_project_b'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.requirement = data['requirement']
        self.description = data['description']
        self.hours = data['hours']
        self.time_frame = data['time_frame']
        self.salary = data['salary']
        self.business_id = data['business_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def create_jobs(cls,data):
        query = "INSERT INTO jobs ( title, requirement, description, hours, time_frame, salary, business_id, created_at, updated_at ) VALUES ( %(title)s, %(requirement)s, %(description)s, %(hours)s, %(time_frame)s, %(salary)s, %(business_id)s, NOW(), NOW());"
        return connectToMySQL(Job.db).query_db(query,data)
    
    @classmethod
    def get_jobs(cls,data):
        query = "SELECT * FROM jobs WHERE business_id = %(business_id)s;"
        results = connectToMySQL(Job.db).query_db(query,data)
        jobs = []
        for job in results:
            jobs.append( cls(job) )
        return jobs
    
    @classmethod
    def get_job(cls,data):
        query = "SELECT * FROM jobs WHERE id = %(id)s;"
        results = connectToMySQL(Job.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM businesses WHERE email = %(eml)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_city(cls,data):
        query = """
                SELECT * FROM jobs
                JOIN businesses on jobs.business_id = businesses.id
                WHERE businesses.city = %(city)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        jobs =[]
        for row in results:
            this_job = cls(row)
            user_data = {
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "business_name": row['business_name'],
                    "address": row['address'],
                    "city": row['city'],
                    "state": row['state'],
                    "password": "",
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
            }
            this_job.creator = business.Business(user_data)

            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_by_state(cls,data):
        query = """
                SELECT * FROM jobs
                JOIN businesses on jobs.business_id = businesses.id
                WHERE businesses.state = %(state)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        jobs =[]
        for row in results:
            this_job = cls(row)
            user_data = {
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "business_name": row['business_name'],
                    "address": row['address'],
                    "city": row['city'],
                    "state": row['state'],
                    "password": "",
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
            }
            this_job.creator = business.Business(user_data)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def  delete(cls,data):
        query = "DELETE FROM jobs WHERE id = %(id)s"
        return connectToMySQL(Job.db).query_db(query,data)
    
    @staticmethod
    def validate_job(user):
        is_valid = True
        if len(user['ttl']) < 4:
            flash("Title must be at least 4 characters","register")
            is_valid = False
        if len(user['req']) < 10:
            flash("Requirements must be at least 10 characters","register")
            is_valid = False
        if len(user['desc']) < 3:
            flash("Description name must be at least 10 characters","register")
            is_valid = False
        if len(user['hrs']) < 1:
            flash("Please input hours","register")
            is_valid = False
        if len(user['tmfm']) < 1:
            flash("Please chose whether the job is contractual or permanent","register")
            is_valid = False
        if len(user['sal']) < 3:
            flash("Salary must be at least 2 characters","register")
            is_valid = False
        return is_valid
    
class Apply:
    db = 'solo_project_b'
    def __init__(self,data):
        self.id = data['id']
        self.job_id = data['job_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.aplicant = None
        self.job = None

    @classmethod
    def create_apply(cls,data):
        query = "INSERT INTO applications ( job_id, user_id, created_at, updated_at ) VALUES ( %(job_id)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(Job.db).query_db(query,data)
    
    
    @classmethod
    def get_applys(cls,data):
        query = """
                SELECT * FROM applications
                JOIN users on applications.user_id = users.id
                WHERE applications.job_id = %(job_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        jobs =[]
        for row in results:
            this_job = cls(row)
            user_data = {
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "birthday": row['email'],
                    "skills": row['email'],
                    "address": row['address'],
                    "city": row['city'],
                    "state": row['state'],
                    "password": "",
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
            }
            this_job.creator = user.User(user_data)

            jobs.append(this_job)
        return jobs
