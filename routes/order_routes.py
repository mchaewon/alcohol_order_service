from flask import render_template, redirect, url_for, session, Blueprint, request, jsonify
from database.db import Oracledb

order_bp = Blueprint('order', __name__)
oracle = Oracledb()

@order_bp.route("/mypage")
def mypage():
  userid = session['userid']
  query = f"select * from CUSTOMER where Customer_ID = '{userid}'"
  result = list(oracle.select(query, 1)[0])
  result[4] = str(result[4]).split()[0]
  return render_template('my_page.html', data = result)

@order_bp.route("/orderlist")
def orderlist():

  return render_template('order_list.html')

@order_bp.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        alhocol_id = request.form.get('id')
        quantity = request.form.get('quantity')
        if 'cart' not in session:
            session['cart'] = []
        t = list(session['cart'])
        t.append([alhocol_id, quantity])
        session['cart'] = t
    return redirect(url_for('order.cart'))

@order_bp.route("/delete_cart", methods=['POST'])
def delete_cart():
    if request.method == 'POST':
        alhocol_id = request.form.get('id')
        quantity = request.form.get('quantity')
        t = list(session['cart'])
        t.remove([alhocol_id, quantity])
        session['cart'] = t
    return redirect(url_for('order.cart'))
       

@order_bp.route("/cart")
def cart():
    cart = session.get('cart', [])
    print(session)
    cartdata = []
    total_price = 0
    for x in cart:
        query = f"select * from ALCOHOL where Alcohol_ID = '{x[0]}'"
        tmp = oracle.select(query, 1)[0]
        print(tmp)
        cartdata.append((tmp[0], tmp[1], tmp[3], x[1], tmp[6] ))
        total_price += (int(x[1]) * tmp[3])
    return render_template('cart.html', data = cartdata, price=total_price)
