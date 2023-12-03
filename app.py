# app.py
from flask import Flask
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.order_routes import order_bp
from config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(order_bp, url_prefix='/')


    return app
