#!/usr/bin/python3
from models import storage
from models.login import UserLogin
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify

@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """register a user"""
    error = None
    content = request.get_json(silent=True)
    password = content.get('password')
    username = content.get('username')
    user_exists = storage.get_user(username, password, UserLogin)
    if user_exists:
        return jsonify("User Exists")
    if request.method == 'POST':
        if type(content) is dict:
            if 'username' in content.keys():
                if 'password' in content.keys():
                    new_user = UserLogin(**content)
                    new_user.save()
                    response = jsonify(new_user.to_dict())
                    response.status_code = 201
                    return response
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
        redirect(url_for("app_views.login"))


