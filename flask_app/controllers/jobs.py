from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User,Trade
from flask_app.models.job import Job,Apply

@app.route ('/new/job')
def job():
    if 'biz_id' not in session:
        return redirect('/')
    return render_template('new_job.html')

@app.route ('/create/job', methods=["POST"])
def create_posting():
    if 'biz_id' not in session:
        return redirect('/')
    if not Job.validate_job(request.form):
        return redirect('/edit/user')
    data = {
        'title' : request.form['ttl'],
        'requirement' : request.form['req'],
        'description': request.form['desc'],
        'hours': request.form['hrs'],
        'time_frame': request.form['tmfm'],
        'salary': request.form['sal'],
        'business_id': session['biz_id']
    }
    Job.create_jobs(data)
    return redirect('/biz/profile')

@app.route ('/dashboard')
def dash():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_user({'id': session['user_id']})
    city = {
        'city': user.city
    }
    state = {
        'state': user.state
    }
    return render_template('dashboard.html', c_jobs = Job.get_by_city(city), s_jobs = Job.get_by_state(state))

@app.route ('/job/<int:num>')
def display_job(num):
    if 'biz_id' not in session:
        return redirect('/')
    return render_template('job.html', job = Job.get_job({'id':num}), applys = Apply.get_applys({'job_id':num}))

@app.route ('/delete/<int:id>')
def delete_job(id):
    Job.delete({'id': id})
    return redirect('/biz/profile')


@app.route ('/jobs/<string:st>')
def city(st):
    if 'user_id' not in session:
        return redirect('/')
    st = {
        'state': st
    }
    return render_template('dashboard.html', s_jobs = Job.get_by_state(st))

@app.route ('/apply/<int:num>')
def creat_application(num):
    data = {
        'job_id': num,
        'user_id': session['user_id']
    }
    Apply.create_apply(data)
    return redirect ('/dashboard')

@app.route ('/applicant/<int:num>')
def view_applicant(num):
    if 'biz_id' not in session:
        return redirect('/')
    data = {
        'id': num
    }
    skills = {
        "user_id": session['user_id']
    }
    return render_template('a_profile.html', user = User.get_user(data), trade = Trade.get_skills(skills))