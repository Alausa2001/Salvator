#!/usr/bin/python3
from flask import Flask, render_template, flash, redirect, url_for
import requests
from templates.forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3ff31a6c7ebd7c9773b8de18bc8ddb13'


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    """ Render the homepage when / or /home is requested """
    return render_template('homepage.html')


@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """ Render the registration form and redirect to login page if successful """
    form = SignUpForm()
    if form.validate_on_submit():
        # Form validation
        data = {
            'username': form.username.data,
            'email': form.email.data,
            'password': form.password.data
        }
        url = 'http://web-02.feranmi.tech/api/v1/register'
        response = requests.post(url, json=data)
        if response.status_code == 200:
            msg = response.json()
            if msg == 'User Exists':
                flash('The username has already been taken. Try a new username', 'danger')
            elif msg == 'Email Exists':
                flash('The email address has already been taken. Try a new email address', 'danger')
        elif response.status_code == 201:
            flash(f"You have successfully created an account! {form.username.data}", 'info')
            return redirect(url_for('home'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'There was an error in creating a new user: {msg[0]}', category='danger')
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ Login User """
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
