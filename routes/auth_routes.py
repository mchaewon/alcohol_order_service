# routes/auth_routes.py
from flask import render_template, request, redirect, url_for, session, Blueprint
from models import User
from config import SECRET_KEY
from database.db import Oracledb

auth_bp = Blueprint('auth', __name__)
oracle = Oracledb()

@auth_bp.route('/login')
def login():
    return render_template('signin.html')

@auth_bp.route('/logout')
def logout():
    if 'userid' in session:
        session.pop('userid', None)
    if 'managerid' in session:
        session.pop('managerid', None)
    return redirect(url_for('auth.login'))


@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')

@auth_bp.route('/signup_process_form', methods=['POST'])
def signup_process_form():
    if request.method == 'POST':
        user_id = request.form.get('id')
        name = request.form.get('name')
        password = request.form.get('password')
        phonenum = request.form.get('phonenum')
        birth = request.form.get('birth')
        address = request.form.get('address')
        info = [user_id, name, password, phonenum, birth, address]
        if oracle.signup(info):
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.signup"))
    else:
        return "invalid access"

@auth_bp.route('/login_process_form', methods=['POST'])
def login_process_form():
    if request.method == 'POST':
        type = request.form.get('type')
        if type == 'customer':
            user_id = request.form.get('id')
            password = request.form.get('password')
            if oracle.authenticate_user(user_id, password):
                session['userid'] = user_id
                return redirect(url_for('main.aftersignin'))
            else:
                return redirect(url_for('auth.login'))
        else: #manager
            manager_id = request.form.get('id')
            manager_name = request.form.get('password')
            if oracle.authenticate_manager(manager_id, manager_name):
                session['managerid'] = (manager_id, manager_name)
                return redirect(url_for('manager.msearch', page_num=1))
            else:
                return redirect(url_for('auth.login'))

    else:
        return "invalid access"
    

