from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User,Trade
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def to_main():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/new/user')
def new_user():
    return render_template('new_user.html')
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
    user = User.create_user(data)
    session['user_id'] = user
    skills ={
        "carpentry": request.form['carp'],
        "cement": request.form['cem'],
        "drywall": request.form['dry'],
        "heavy_machinery": request.form['hvmc'],
        "high_v_electrivity": request.form['high'],
        "home_electricity": request.form['home'],
        "hvac": request.form['hvac'],
        "plumbing": request.form['plmg'],
        "user_id": session['user_id']
    }
    User.save_skills(skills)
    return redirect('user/profile')

app.route('/user/profile')
def prof():

    return render_template( 'profile.html')

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