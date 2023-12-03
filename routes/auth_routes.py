# routes/auth_routes.py
from flask import render_template, request, redirect, url_for, session
from models import User
from config import SECRET_KEY

from app import app, oracle

@app.route('/login')
def login():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login_process_form', methods=['POST'])
def login_process_form():
    if request.method == 'POST':
        user_id = request.form.get('id')
        password = request.form.get('password')
        if oracle.authenticate_user(user_id, password):
            session['userid'] = user_id
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))
