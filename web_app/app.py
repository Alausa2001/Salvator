from flask import Flask, render_template, flash, redirect, url_for, session, Blueprint
from auth import bp
from blog import bg


app = Flask(__name__)
app.config['SECRET_KEY'] = '3ff31a6c7ebd7c9773b8de18bc8ddb13'
app.register_blueprint(bp)
app.register_blueprint(bg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
