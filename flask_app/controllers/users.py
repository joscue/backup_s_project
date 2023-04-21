from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User,Trade
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def to_main():
    if 'user_id' in session:
        return redirect('/user/profile')
    if 'biz_id' in session:
        return redirect('/biz/profile')
    return render_template('index.html')

@app.route('/new/user')
def new_user():
    if 'user_id' in session:
        return redirect('/user/profile')
    if 'biz_id' in session:
        return redirect('/biz/profile')
    return render_template('new_user.html')

@app.route('/user/register',methods=["POST"])
def register_user():
    if 'user_id' in session:
        return redirect('/user/profile')
    if 'biz_id' in session:
        return redirect('/biz/profile')
    if not User.validate_register(request.form):
        return redirect('/new/user')    
    data ={
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "birthday": request.form['bday'],
        "skills": request.form['desc'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
        "password": bcrypt.generate_password_hash(request.form['pswd'])
    }
    user = User.create_user(data)
    session['user_id'] = user
    skills ={
        "carpentry": request.form['carp'],
        "cement": request.form['cem'],
        "drywall": request.form['dry'],
        "heavy_machinery": request.form['hvmc'],
        "high_v_electricity": request.form['high'],
        "home_electricity": request.form['home'],
        "hvac": request.form['hvac'],
        "plumbing": request.form['plmg'],
        "user_id": session['user_id']
    }
    Trade.save_skills(skills)
    return redirect('/user/profile')

@app.route('/edit/user')
def edit_user():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('update_user.html')

@app.route('/user/update',methods=["POST"])
def update_user():
    if 'user_id' not in session:
        return redirect('/')
    if not User.validate_update(request.form):
        return redirect('/edit/user')
    data ={
        'id': session['user_id'],
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "birthday": request.form['bday'],
        "skills": request.form['desc'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
    }
    User.update_user(data)
    skills ={
        "carpentry": request.form['carp'],
        "cement": request.form['cem'],
        "drywall": request.form['dry'],
        "heavy_machinery": request.form['hvmc'],
        "high_v_electricity": request.form['high'],
        "home_electricity": request.form['home'],
        "hvac": request.form['hvac'],
        "plumbing": request.form['plmg'],
        "user_id": session['user_id']
    }
    Trade.update_skills(skills)
    return redirect('/user/profile')

@app.route('/user/login',methods=["POST"])
def ulogin():
    if 'user_id' in session:
        return redirect('/user/profile')
    if 'biz_id' in session:
        return redirect('/biz/profile')
    job = User.get_by_email(request.form)
    if not job:
        flash("Invalid Email","ulogin")
        return redirect('/')
    if not bcrypt.check_password_hash(job.password, request.form['pswd']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = job.id
    return redirect('/user/profile')

@app.route('/user/profile')
def prof():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        "id": session['user_id']
    }
    skills = {
        "user_id": session['user_id']
    }
    return render_template('profile.html', user = User.get_user(data), trade = Trade.get_skills(skills))

@app.route('/user/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/')