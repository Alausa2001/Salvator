#!/usr/bin/python3
from flask import make_response, request, jsonify, abort
from models import storage
from models.login import UserLogin
from models.user_med_info import UserMedInfo
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """returns all users"""
    users = []
    for user in storage.all("UserLogin").values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/biodata/<username>', methods=['POST'], strict_slashes=False)
def input_biodata(username):
    """handles entering of user's biodata"""
    compulsory = ['first_name', 'last_name', 'age', 'genotype', 'blood_group']
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    user_id = user.id
    username_exists = user.username
    if username_exists == username:
        userdata = request.get_json(silent=True)
        if type(userdata) is not dict:
            return make_response(jsonify("Not a JSON"), 400)
        for data in compulsory:
            if data not in userdata:
                return make_response(jsonify(f"{data} is missing"), 400)
        biodata = UserMedInfo(**userdata)
        setattr(biodata, 'med_id', user_id)
        biodata.save()
        return make_response(jsonify(biodata.to_dict()), 201)


@app_views.route('/biodata/<username>', methods=['GET'], strict_slashes=False)
def get_biodata(username):
    """gets a user's biodata"""
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    med_id = user.id
    user_biodata = storage.get_biodata(med_id, UserMedInfo)
    if not user_biodata:
        return jsonify("Record not found")
    return make_response(jsonify(user_biodata.to_dict()), 200)


@app_views.route('/biodata/<username>', methods=['PUT'], strict_slashes=False)
def update_biodata(username):
    """updates a user's biodata"""
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    med_id = user.id
    user_biodata = storage.get_biodata(med_id, UserMedInfo)
    if not user_biodata:
        return jsonify("Record not found")
    update_data = request.get_json(silent=True)
    if type(update_data) is not dict:
        return jsonify("Not a JSON")
    for key, value in request.json.items():
        setattr(user_biodata, key, value)
    user_biodata.save()
    return make_response(jsonify(user_biodata.to_dict()), 200)


@app_views.route('biodata/<username>', methods=['DELETE'],
                 strict_slashes=False)
def delete_biodata(username):
    """deletes a user's data"""
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    med_id = user.id
    user_biodata = storage.get_biodata(med_id, UserMedInfo)
    if not user_biodata:
        return jsonify("Record not found")
    storage.delete(user_biodata)
    storage.save()
    return jsonify("Deleted Successfully")
