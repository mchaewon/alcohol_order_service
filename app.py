from flask import Flask
from flask import render_template, request, redirect, url_for, session

import cx_Oracle

app = Flask(__name__)
app.secret_key = 'your_secret_key'

'''
sample user id / pw
JzUx2510 / nMczX8294
TdlZ4221 / hotly4729
'''

class user:
    def __init__(self):
        self.userid = None
        self.phonenum = None
        self.name = None
        self.birth = None
        self.address = None
    
    def getcurrentuserinfo(self):
        self.userid = session['userid']
        info = oracle.getuserinfo(self.userid)
        self.name = info[2]
        self.phonenum = info[3]
        self.birth = info[4]
        self.address = info[5]
        return self.userid
        


class oracledb:
    def __init__(self):
        db_config = {
            'user':'alcohol',
            'password':'comp322'
        }
        conn = cx_Oracle.connect(**db_config)
        self.cursor = conn.cursor()
    
    def select(self, query, size):
        self.cursor.execute(query)
        return self.cursor.fetchmany(size)
    

    def authenticate_user(self, userid, password):
        query = f"SELECT count(*) FROM CUSTOMER WHERE Customer_ID='{userid}' AND Password='{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] > 0
    
    def getuserinfo(self, userid):
        query = f"select * from CUSTOMER where Customer_ID = '{userid}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def closedb(self):
        self.cursor.close()

@app.route('/')
def main():
    if 'userid' in session:
        query = 'select * from ALCOHOL'
        result = oracle.select(query, 12)
        return render_template('index.html', data=result)
    else:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login_process_form', methods=['POST'])
def login_process_form():
    if request.method == 'POST':
        user_id = request.form.get('id')
        password = request.form.get('password')
        if oracle.authenticate_user(user_id, password):
            session['userid'] = user_id
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    
    session.pop('userid', None)
    return redirect(url_for('login'))    

@app.route('/cover')
def cover():
    return render_template('cover.html')

# 웹 애플리케이션을 실행합니다.
if __name__ == '__main__':
    oracle = oracledb()
    currentuser = user()
    app.run(debug=True)
