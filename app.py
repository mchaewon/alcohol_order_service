from flask import Flask
from flask import render_template

import cx_Oracle

app = Flask(__name__)

db_config = {
  'user':'alcohol',
  'password':'comp322'
}

def connectdb():
    query = 'select * from ALCOHOL'
    conn = cx_Oracle.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

def get_data(cursor):
    result = cursor.fetchone()
    print(result)
    return result


@app.route('/')
def main():
    cursor = connectdb()
    data = []
    for _ in range(10):
        result = get_data(cursor=cursor)
        data.append(result)
    print(result)
    return render_template('index.html', data = data)

@app.route('/sign')
def sign():
    return render_template('signin.html')

@app.route('/cover')
def cover():
    return render_template('cover.html')

# 웹 애플리케이션을 실행합니다.
if __name__ == '__main__':
    app.run(debug=True)
