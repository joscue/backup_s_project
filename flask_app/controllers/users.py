from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def to_main():
    return render_template('index.html')

@app.route ('/dashboard')
def dash():
    return render_template('dashboard.html')