# routes/main_routes.py
from flask import render_template, redirect, url_for, session
from app import app, oracle

@app.route('/')
def main():
    if 'userid' in session:
        query = 'select * from ALCOHOL'
        result = oracle.select(query, 12)
        return render_template('index.html', data=result)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('login'))

@app.route('/cover')
def cover():
    return render_template('cover.html')
