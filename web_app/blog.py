import functools
from flask import abort, Blueprint, flash, g, redirect, render_template, session, url_for, jsonify
from web_app.forms import BiodataForm, MedicalRecordForm
import requests


bg = Blueprint('blog', __name__)


def send_to_database(url, data, msg):
    """ Send data to the url passed """
    # Update the database with the new data
    requests.post(url, json=data)
    flash(msg, 'success')
    return redirect(url_for('blog.dashboard'))

def flash_error(error_msg):
    """ Flash the error messages passed as an argument """
    if error_msg != {}:
        for field, msg in error_msg.items():
            flash(f'{field.upper()} : {msg[0]}', category='danger')

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
    record = MedicalRecordForm()
    username = session['username']
    # BIODATA UPDATE
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
        bio_msg = f'Your biodata has been successfully updated! 🌟'
        url = f'http://web-02.feranmi.tech/api/v1/biodata/{username}'
        # Update the database with the biodata
        send_to_database(url=url, data=bio, msg=bio_msg)
    if g.user['biodata'].get('alert'):
        flash_error(bioform.errors)
    # RECORD UPDATE
    if record.validate_on_submit():
        print(record.date.data)
        obj = jsonify({
            'date': record.date.data,
            'diagnosis': record.diagnosis.data,
            'prescription': record.prescription.data
        })
        new_record = obj.json
        record_msg = f'The new record is added successfully! 🌟'
        record_url = f'http://web-02.feranmi.tech/api/v1/record/{username}'
        # Update the database with the new record
        send_to_database(url=record_url, data=new_record, msg=record_msg)
        return redirect(url_for('blog.dashboard'))
    if record.errors != {} and record.is_submitted():
        flash_error(record.errors)
    return render_template('blog/dashboard.html', bioform=bioform, record=record)


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