from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def to_main():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/user/register',methods=["POST"])
def ureg():
    if not User.validate_register(request.form):
        return redirect('/')
    data ={
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "birthday": request.form['bday'],
        "skills": request.form['skl'],
        "resume": request.form['rsm'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
        "password": request.form['pswd']
    }
    user = User.save(data)
    session['user_id'] = user
    
    return redirect('user/id/profile')

app.route('/user/id/profile')
def prof():

    return render_template( 'profile.html', user = User.get_user({"id":session['user_id']}) )

app.route('/create/profile')
def create_prof():
#   need validation
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "business_name": request.form['bname'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['state'],
        "email": request.form['eml'],
    }