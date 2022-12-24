#!/usr/bin/python3
from models import storage
from models.login import UserLogin
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify
from models.med_records import Records
from models.user_med_info import UserMedInfo


@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """register a user"""
    error = None
    content = request.get_json(silent=True)
    password = content.get('password')
    username = content.get('username')
    user_exists = storage.get_user(username, UserLogin)
    if user_exists:
        return jsonify("User Exists")
    if request.method == 'POST':
        if type(content) is dict:
            if 'username' in content.keys():
                if 'password' in content.keys():
                    if 'email' in content.keys():
                        new_user = UserLogin(**content)
                        new_user.save()
                        response = jsonify(new_user.to_dict())
                        response.status_code = 201
                        return response
                    else:
                        error = "missing email"
                else:
                    error = "missing password"
            else:
                error = "missing username"
        else:
            error = "Not a JSON"
        response = jsonify(error)
        response.status_code = 400
        return response
    else:
        # redirect(url_for("app_views.login"))
        pass

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """return users details (biodata and medical records), when they login"""
    login_details = request.get_json(silent=True)
    if type(login_details) is not dict:
        return jsonify("Not a JSON")
    username = login_details.get('username')
    password = login_details.get('password')
    email = login_details.get('email')
    if username:
        user = storage.get_user(username, UserLogin)
    if username is None and email is not None:
        user = storage.get_user_via_email(email, password, UserLogin)
    if not user:
        return make_response(jsonify("User does not exists"), 404)
    if password != user.password:
        return make_response(jsonify("Wrong password"), 400)

    # get a user's biodata
    med_id = user.id
    user_biodata = storage.get_biodata(med_id, UserMedInfo)
    if not user_biodata:
        biodata = {"alert" : "You are yet to fill in your biodata"}
    if type(biodata) is not dict:
        biodata = user_biodata.to_dict()

    # """get a user's medical records"""
    all_records = []
    user_id = user.id
    records = storage.get_record(user_id, Records)
    if not records:
        all_records = {"alert": "You have no saved biodata"}
    if type(all_records) is not dict:
        for record in user.records:
            all_records.append(record.to_dict())
    return jsonify({"biodata": biodata, "medical_records": all_records})
