import requests
from flask import render_template, flash, redirect, url_for, session, Blueprint
from forms import SignUpForm, LoginForm 
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


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
            flash(f"You have successfully created an account! {form.username.data}", 'success')
            return redirect(url_for('blog.home'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'There was an error in creating a new user: {msg[0]}', category='danger')
    return render_template('auth/signup.html', form=form)


@bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ Login User """
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for(f'dashboard/{form.username.data}'))
    return render_template('auth/login.html', form=form)


@bp.route('/logout', strict_slashes=False)
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('blog.home'))