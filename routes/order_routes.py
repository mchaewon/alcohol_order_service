from flask import render_template, redirect, url_for, session, Blueprint, request, jsonify
from database.db import Oracledb

order_bp = Blueprint('order', __name__)
oracle = Oracledb()

@order_bp.route("/mypage")
def mypage():
  return render_template('my_page.html')


@order_bp.route("/orderlist")
def orderlist():
  return render_template('order_list.html')

@order_bp.route("/cart")
def cart():
  return render_template('cart.html')
