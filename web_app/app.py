#!/usr/bin/python3
"""
    Flask Application Loader
"""

import requests
from flask import Flask, render_template, url_for, redirect
from templates.forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'faa0ea78c2abe69f3b84a17dd885198c'


@app.route('/', strict_slashes=False)
@app.route('/homepage', strict_slashes=False)
def homepage():
    return render_template('homepage.html', title='HOME')

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    form = LoginForm()
    r = requests.get('http://web-02.feranmi.tech/api/v1/users')
    data = r.json()
    form.validate_on_submit()
    for user in data:
        if user.get('username') == form.username.data and user.get('password') == form.password.data:
            return redirect(url_for('dashboard'))
    return render_template('login.html', title='LOGIN', form=form)


@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignUpForm()
    return render_template('signup.html', title='SIGNUP', form=form)

@app.route('/dashboard', methods=['GET', 'POST', 'DELETE', 'PUT'])
def dashboard():
    return render_template('dashboard.html', title='DASHBOARD')

if __name__ == "__main__":
    app.run(debug=True)