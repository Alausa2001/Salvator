from web_app.auth import load_logged_in_user
import functools
from flask import abort, Blueprint, flash, g, redirect, render_template, session, url_for
from web_app.forms import BiodataForm
import requests


bg = Blueprint('blog', __name__)


def login_required(view):
    """ Decorator to check if user is available or Not"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('You are not logged in', 'danger')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bg.route('/', strict_slashes=False)
@bg.route('/home', strict_slashes=False)
def home():
    """ Render the homepage when / or /home is requested """
    return render_template('blog/homepage.html')


@bg.route('/dashboard', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def dashboard():
    """ Display user informations """
    bioform = BiodataForm()
    if bioform.validate_on_submit():
        bio = {
            'first_name': bioform.firstname.data,
            'last_name': bioform.lastname.data,
            'age': bioform.age.data,
            'genotype': bioform.genotype.data.upper(),
            'blood_group': bioform.bloodgroup.data.upper(),
            'height': bioform.height.data,
            'weight': bioform.weight.data,
            'allergies': bioform.allergies.data
        }
        username = session['username']
        # Update the database with the biodata
        url = f'http://web-02.feranmi.tech/api/v1/biodata/{username}'
        response = requests.post(url, json=bio)
        # load_logged_in_user()
        flash(f'Your biodata has been successfully updated! 🌟', 'success')
        return redirect(url_for('blog.dashboard'))
    if bioform.errors != {}:
        for field, msg in bioform.errors.items():
            flash(f'{field.upper()} : {msg[0]}', category='danger')
    return render_template('blog/dashboard.html', bioform=bioform)


@bg.route('/account', strict_slashes=False)
@login_required
def account():
    """ Access account informations with this endpoint """
    return render_template('blog/dashboard.html',)


@bg.route('/records', strict_slashes=False)
@login_required
def records():
    """ Display the medical records """
    abort(404, f"Coming soon...")