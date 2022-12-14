#!/usr/bin/python3
from flask import Flask, request, jsonify, make_response, abort, render_template
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
# app.config('JSONIFY_PRETTYPRINT_REGULAR') = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """closes database on teardown"""
    storage.close()

@app.errorhandler(404)
def notfound(msg):
    """handles 404 errors"""
    return make_response(jsonify({'err 404': 'not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

