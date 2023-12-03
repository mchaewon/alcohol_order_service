# routes/main_routes.py
from flask import render_template, redirect, url_for, session, Blueprint
from database.db import Oracledb

main_bp = Blueprint('main', __name__)
oracle = Oracledb()

@main_bp.route('/')
def main():
    if 'userid' in session:
        query = 'SELECT * FROM ALCOHOL'
        result = oracle.select(query, 12)
        return render_template('index.html', data=result)
    else:
        return redirect(url_for('auth.login'))


@main_bp.route('/cover')
def cover():
    return render_template('cover.html')
