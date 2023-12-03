# app.py
from flask import Flask
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.order_routes import order_bp
from config import SECRET_KEY
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.permanent_session_lifetime = timedelta(minutes=30) 
    app.config['SESSION_TYPE'] = 'filesystem'  # 파일 시스템에 저장



    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(order_bp, url_prefix='/')


    return app
