from flask import render_template, request, redirect, url_for, session, Blueprint
from models import User
from config import SECRET_KEY
from database.db import Oracledb

manager_bp = Blueprint('manager', __name__)
oracle = Oracledb()

@manager_bp.route('/msearch/<int:page_num>')
def msearch(page_num):
  name = session['managerid'][1]
  query = f"SELECT * FROM NOTICE N where writer = '{name}' order by written_date desc"
  result = oracle.selectall(query)
  page, result = oracle.selectpage(query, 20, page_num)
  return render_template('manager_search.html', page=page, data=result)

@manager_bp.route('/mwrite')
def mwrite():
  from datetime import datetime
  current_date = datetime.now().strftime('%Y-%m-%d')
  return render_template('manager_write.html', time=current_date)

@manager_bp.route('/write_process', methods=['GET', 'POST'])
def write_process():
  import random
  import string
  def generate_random_id(length=8):
        characters = string.ascii_letters + string.digits
        random_id = ''.join(random.choice(characters) for _ in range(length))
        return random_id
  
  name = request.form.get('name')
  date = request.form.get('date')
  content = request.form.get('contents')
  noticeresult = 1
  while noticeresult == 1:
      noticeid = generate_random_id()
      orderquery = f"SELECT Count(*) FROM notice WHERE Notice_ID = '{noticeid}'"
      noticeresult = oracle.select(orderquery, 1)[0]

  info = [noticeid, name, date, content]
  
  oracle.notice_insert(info)
  return redirect(url_for('manager.msearch', page_num=1))

  
@manager_bp.route('/delete_process', methods=['POST'])
def delete_process():
  noticeid = request.form.get('noticeid')
  managerid = session['managerid'][0]
  oracle.notice_delete(noticeid, managerid)
  return redirect(url_for('manager.msearch', page_num=1))