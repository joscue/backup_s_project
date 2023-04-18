from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.business import Business
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new/biz')
def new_biz():
    return  render_template('new_biz.html')

@app.route('/register/business',methods=["POST"])
def breg():

    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "business_name": request.form['bname'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
        "password": request.form['pswd']
    }
    biz = Business.create_biz(data)
    session['biz_id'] = biz
    return redirect('/biz/profile')

@app.route('/biz/profile')
def bprof():
    return render_template('b_profile.html', biz = Business.get_biz({'id': session['biz_id']}))