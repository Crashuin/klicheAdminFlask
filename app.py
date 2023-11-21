from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import abort

app = Flask(__name__)
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/dashboard/inicio')
def dashboard():
    return render_template('dashboard/inicio.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
