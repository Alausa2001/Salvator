#!/usr/bin/python3
from models import storage
from models.login import UserLogin
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify

@app_views.route('/register', methods=['POST'], strict_slashes=False)
def register():
    """register a user"""
    if request.method == 'POST':
        """
        content = request.get_json(silent=True)
        error = ""
        if type(content) is dict:
            new_user = UserLogin(**content)
            new_user.save()
            response = jsonify(new_user.to_dict())
            response.status_code = 201
            return response
        else:
            error = "Not a JSON"
        response = jsonify(error_message)
        response.status_code = 400
        return response
        """
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = "missing username"
        elif not password:
            error = "mising password"
        if error is None:
            new_user = UserLogin(username, password)
            new_user.save()
            response = jsonify(new_user.to_dict())
            response.status_code = 201
            return response
        else:
            return jsonify(error)
