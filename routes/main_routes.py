# routes/main_routes.py
from flask import render_template, redirect, url_for, session, Blueprint, request
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

@main_bp.route('/search')
def search():
    return render_template('search.html')

@main_bp.route('/search_condition', methods=['GET'])
def search_condition():
    beer_type = request.args.get('beerType')
    beer_name = request.args.get('beerName')
    price = request.args.get('price')
    star = request.args.get('selectedStars')
    return redirect(url_for('main.main'))

@main_bp.route('/cover')
def cover():
    return render_template('cover.html')
