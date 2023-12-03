# routes/main_routes.py
from flask import render_template, redirect, url_for, session, Blueprint, request, jsonify
from database.db import Oracledb

main_bp = Blueprint('main', __name__)
oracle = Oracledb()

@main_bp.route('/')
def main():
    if 'userid' in session:
        type_param = request.args.get('type', default='all', type=str)
        if type_param == 'all':
            query = "SELECT A.Name, A.Price, A.Alcohol_degree, A.Type, round(avg(P.Star_rating),1) AS star FROM ALCOHOL A, POINT P WHERE A.Alcohol_ID=P.Alcohol_ID group by A.Name, A.Price, A.Alcohol_degree, A.Type"
        elif type_param == 'etc':
            l = "('soju', 'beer', 'makgeolli', 'wine', 'sake', 'whiskey', 'tequila', 'brandy', 'gin', 'rum')"
            query = f"SELECT A.Name, A.Price, A.Alcohol_degree, A.Type, ROUND(AVG(P.Star_rating), 1) AS Avg_Star_Rating FROM ALCOHOL A JOIN POINT P ON A.Alcohol_ID = P.Alcohol_ID WHERE lower(A.Type) NOT IN {l} GROUP BY A.Name, A.Price, A.Alcohol_degree, A.Type"
        else:
            query = f"SELECT A.Name, A.Price, A.Alcohol_degree, A.Type, round(avg(P.Star_rating),1) FROM ALCOHOL A, POINT P WHERE A.Alcohol_ID=P.Alcohol_ID and type like '%{type_param}%' group by A.Name, A.Price, A.Alcohol_degree, A.Type"
        print(query)
        result = oracle.select(query, 12)

        return render_template('index.html', data=result)
    else:
        return redirect(url_for('auth.login'))
    

@main_bp.route('/search')
def search():
    return render_template('search.html')

@main_bp.route('/sample')
def sample():
    return render_template('sample.html')

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

@main_bp.route('/notice')
def notice():
    return render_template('notice.html')

@main_bp.route('/find')
def find():
    return render_template('search.html')

@main_bp.route('/store')
def store():
    return render_template('store.html')
