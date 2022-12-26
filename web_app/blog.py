from flask import render_template, flash, redirect, url_for, session, Blueprint

bg = Blueprint('blog', __name__, url_prefix='/blog')


@bg.route('/', strict_slashes=False)
@bg.route('/home', strict_slashes=False)
def home():
    """ Render the homepage when / or /home is requested """
    return render_template('blog/homepage.html')


@bg.route('/dashboard/<username>', strict_slashes=False)
def dashboard(username):
    """ Display user informations """
    if username in session:
        profile = {'user': username }
        return render_template('dashboard.html', user=profile.get('user'))
    flash('You are not logged in', 'danger')
    return redirect(url_for('blog.home'))


