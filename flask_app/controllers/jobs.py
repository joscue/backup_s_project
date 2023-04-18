from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User,Trade

@app.route ('/post/job')
def job():
    return render_template('new_job.html')