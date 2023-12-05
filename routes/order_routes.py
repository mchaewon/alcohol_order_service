from flask import render_template, redirect, url_for, session, Blueprint, request, jsonify
from database.db import Oracledb

order_bp = Blueprint('order', __name__)
oracle = Oracledb()

import random
import string

def generate_random_id(length=8):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

@order_bp.route("/mypage")
def mypage():
  userid = session['userid']
  query = f"select * from CUSTOMER where Customer_ID = '{userid}'"
  result = list(oracle.select(query, 1)[0])
  result[4] = str(result[4]).split()[0]
  return render_template('my_page.html', data = result)

@order_bp.route("/orderlist")
def orderlist():
  userid = session['userid']

  query = f"SELECT A.Name, A.Type, A.Price, ICB.Quantity, ICB.Total_price, TRUNC(O.Order_date) as Order_date, O.Order_ID, A.Picture, A.Alcohol_ID, P.Star_rating FROM ORDERS O JOIN IS_CONTAINED_BY ICB ON O.Order_ID = ICB.Order_ID JOIN ALCOHOL A ON A.Alcohol_ID = ICB.Alcohol_ID LEFT JOIN POINT P ON O.Customer_ID = P.Customer_ID AND P.Alcohol_ID = A.Alcohol_ID WHERE O.Customer_ID='{userid}' ORDER BY O.Order_date DESC"
  
  print(query)

  result = oracle.selectall(query)
  print(result)
  return render_template('order_list.html', data = result)




@order_bp.route("/order")
def order():
    from datetime import datetime
    import random
    import string

    current_date = datetime.now().strftime('%Y-%m-%d')
    userid = session['userid']

    #orders, is_contained_by 에 항목을 넣어야함.

    #orders : orderid, customer_id, store_id, current_date
    while len(session['cart']) != 0: # session 의 항목 개수만큼 반복 실행
        x = session['cart'][-1] # alcohol_id, quantity
        
        #랜덤 orderid 생성
        orderresult = 1
        while orderresult == 1:
            orderid = generate_random_id()
            orderquery = f"SELECT Count(*) FROM ORDERS WHERE Order_ID = '{orderid}'"
            orderresult = oracle.select(orderquery, 1)[0]

        # 가게 배정
        storequery = "SELECT Store_ID FROM STORE ORDER BY DBMS_RANDOM.VALUE"
        storeid = oracle.select(storequery, 1)[0]
        
        infoorder = [orderid, userid, storeid, current_date]

        # 삽입
        if oracle.order_insert(infoorder):
           
           # order 성공시 is_contained_by 삽입 
           # ICB :  alcoholid, orderid, quantity, total_price

            # alcohol_id로 alcohol price 찾기
            q =  f"SELECT Alcohol_ID, price FROM ALCOHOL WHERE Alcohol_ID = '{x[0]}'"
            uniprice = oracle.select(q, 1)[0]

            total_price = int(x[1]) * int(uniprice[1])

            infoICB = [x[0], orderid, int(x[1]), total_price]

            t = list(session['cart'])
            t.pop()
            session['cart'] = t

            if not oracle.ICB_insert(infoICB):
                return redirect(url_for("order.cart"))
        else:
            return redirect(url_for("order.cart"))
            
    return redirect(url_for("order.orderlist"))

    
        

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
    cartdata = []
    total_price = 0
    for x in cart:
        query = f"select * from ALCOHOL where Alcohol_ID = '{x[0]}'"
        tmp = oracle.select(query, 1)[0]
        print(x)
        cartdata.append((tmp[0], tmp[1], tmp[3], int(x[1]), tmp[6] ))
        total_price += (int(x[1]) * int(tmp[3]))
    return render_template('cart.html', data = cartdata, price=total_price)
