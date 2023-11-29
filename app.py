from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('signin.html')

@app.route('/cover')
def cover():
    return render_template('cover.html')

# 웹 애플리케이션을 실행합니다.
if __name__ == '__main__':
    app.run(debug=True)
