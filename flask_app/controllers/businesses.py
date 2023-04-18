from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new/biz')
def new_biz():
    return  render_template('new_biz.html')
#    data = {
#        "first_name": request.form['fname'],
#        "last_name": request.form['lname'],
#        "business_name": request.form['bname'],
#        "address": request.form['adrs'],
#        "city": request.form['city'],
#        "state": request.form['state'],
#        "email": request.form['eml'],
#    }