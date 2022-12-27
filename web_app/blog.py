import functools
from flask import abort, Blueprint, flash, g, redirect, render_template, session, url_for


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


@bg.route('/dashboard', strict_slashes=False)
@login_required
def dashboard():
    """ Display user informations """
    return render_template('blog/dashboard.html')


@bg.route('/account', strict_slashes=False)
@login_required
def account():
    """ Access account informations with this endpoint """
    return render_template('blog/dashboard.html')


@bg.route('/records', strict_slashes=False)
@login_required
def records():
    """ Display the medical records """
    abort(404, f"Coming soon...")