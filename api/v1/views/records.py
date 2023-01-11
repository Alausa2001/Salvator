#!/usr/bin/python3
from flask import jsonify, make_response, abort, request
from models.login import UserLogin
from models import storage
from models.med_records import Records
from api.v1.views import app_views


@app_views.route('/record/<username>', methods=['POST'], strict_slashes=False)
def enter_records(username):
    """to create medical records"""
    compulsory = ['date', 'diagnosis', 'prescription']
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    user_id = user.id
    username_exists = user.username
    if username_exists == username:
        input_records = request.get_json(silent=True)
        if type(input_records) is not dict:
            return make_response(jsonify("NOT A JSON"), 400)
        for data in compulsory:
            if data not in input_records:
                return make_response(jsonify("{} is missing".format(data)), 400)
        records = Records(**input_records)
        setattr(records, 'records_id', user_id)
        records.save()
        return make_response(jsonify(records.to_dict()), 201)


@app_views.route('/records/<username>', methods=['GET'], strict_slashes=False)
def retrieve_records(username):
    """get a user's medical records"""
    all_records = []
    user = storage.get_user(username, UserLogin)
    if not user:
        abort(404)
    user_id = user.id
    records = storage.get_record(user_id, Records)
    if not records:
        return make_response(jsonify("You have no saved record"), 400)
    for record in user.records:
        all_records.append(record.to_dict())
    return jsonify(all_records)


@app_views.route('record/<id>/<username>', methods=['GET'],
                 strict_slashes=False)
def get_a_record(id, username):
    """get the specified record"""
    user = storage.get_user(username, UserLogin)
    record = storage.get(Records, id)
    if not record:
        return make_response(jsonify("Record not found"), 404)
    if not user:
        abort(404)
    for record in user.records:
        if record.id == id:
            return jsonify(record.to_dict())


@app_views.route('record/<id>/<username>', methods=['PUT'],
                 strict_slashes=False)
def update_records(id, username):
    """update a user's medical records"""
    user = storage.get_user(username, UserLogin)
    record = storage.get(Records, id)
    if not record:
        return make_response(jsonify("Record not found"), 404)
    if not user:
        abort(404)

    updates = request.get_json(silent=True)
    if type(updates) is not dict:
        return make_response(jsonify("Not a JSON"), 400)
    for key, val in updates.items():
        setattr(record, key, val)
    record.save()
    return make_response(jsonify(record.to_dict()), 200)


@app_views.route('record/<id>/<username>', methods=['DELETE'],
                 strict_slashes=False)
def delete_record(id, username):
    """deletes a user"""
    user = storage.get_user(username, UserLogin)
    record = storage.get(Records, id)
    if not record:
        return make_response(jsonify("Record not found"), 404)
    if not user:
        abort(404)
    storage.delete(record)
    storage.save()
    return jsonify("Deleted Successfully")
