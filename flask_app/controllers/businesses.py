from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.business import Business
from flask_app.models.job import Job
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new/biz')
def new_biz():
    if 'user_id' in session:
        return redirect('/user/profile')
    if 'biz_id' in session:
        return redirect('/biz/profile')
    return  render_template('new_biz.html')

@app.route('/register/business',methods=["POST"])
def breg():
    if not Business.validate_register(request.form):
        return redirect('/new/biz')
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "business_name": request.form['bname'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
        "password": bcrypt.generate_password_hash(request.form['pswd'])
    }
    biz = Business.create_biz(data)
    session['biz_id'] = biz
    return redirect('/biz/profile')

@app.route('/edit/biz')
def edit_biz():
    if 'biz_id' not in session:
        return redirect('/')
    return  render_template('update_biz.html')

@app.route('/biz/update',methods=["POST"])
def update_business():
    if 'biz_id' not in session:
        return redirect('/')
    if not Business.validate_update(request.form):
        return redirect('/edit/biz')
    data = {
        'id': session['biz_id'],
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['eml'],
        "business_name": request.form['bname'],
        "address": request.form['adrs'],
        "city": request.form['city'],
        "state": request.form['st'],
    }
    Business.update_biz(data)
    return redirect('/biz/profile')

@app.route('/biz/profile')
def bprof():
    if 'biz_id' not in session:
        return redirect('/')
    return render_template('b_profile.html', biz = Business.get_biz({'id': session['biz_id']}), jobs = Job.get_jobs({'business_id': session['biz_id']}))

@app.route('/biz/login',methods=["POST"])
def login():
    job = Business.bget_by_email(request.form)
    if not job:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(job.password, request.form['pswd']):
        flash("Invalid Password","login")
        return redirect('/')
    session['biz_id'] = job.id
    return redirect('/biz/profile')

@app.route('/biz/logout')
def blogout():
    if 'biz_id' in session:
        session.pop('biz_id')
    return redirect('/')
