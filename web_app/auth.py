from flask import Blueprint, flash, g, redirect, render_template, session, url_for
from forms import LoginForm, SignUpForm
import requests
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    """ Loads logged in user from session before rendering any views"""
    username = session.get('username')
    if username is None:
        g.user = None
    else:
        email = session.get('email')
        password = session.get('password')
        data = {
            'username': username,
            'email': email,
            'password': password
        }
        url = 'http://web-02.feranmi.tech/api/v1/login'
        response = requests.post(url, json=data)
        user_data = {'details': {'username': username, 'email': email}}
        info = response.json()
        user_data['biodata'] = info.get('biodata')
        user_data['records'] = info.get('medical_records')
        g.user = user_data


@bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ Login User """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        url = 'http://web-02.feranmi.tech/api/v1/users'
        response = requests.get(url)
        # Validate if user is already registered
        users = response.json()
        for user in users:
            usr = user['username']
            pwd = user['password']
            em = user['email']
            if username == usr or email == em:
                if check_password_hash(pwd, password):
                    session.clear()
                    session['username'] = username
                    session['email'] = email
                    session['password'] = pwd
                    flash(f'You are now logged in as {username} 😎', 'success')
                    return redirect(url_for(f'blog.dashboard'))
                else:
                    flash('Your password is incorrect', 'danger')
                    return redirect(url_for('auth.login'))
        flash(f'User {username} is not registered', 'danger')
    if form.errors != {}:
        for field, msg in form.errors.items():
            flash(f'{field.upper()} : {msg[0]}', category='danger')
    return render_template('auth/login.html', form=form)


@bp.route('/logout', strict_slashes=False)
def logout():
    # remove the id from the session if it's there
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))


@bp.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """ Render the registration form and redirect to login page if successful """
    form = SignUpForm()
    if form.validate_on_submit():
        # Form validation
        data = {
            'username': form.username.data,
            'email': form.email.data,
            'password': generate_password_hash(form.password.data)
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
            flash(f"You have successfully created an account! {form.username.data} 🎉🎉", 'success')
            return redirect(url_for('auth.login'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'There was an error in creating a new user: {msg[0]}', category='danger')
    return render_template('auth/signup.html', form=form)