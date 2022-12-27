from auth import bp
from blog import bg
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '3ff31a6c7ebd7c9773b8de18bc8ddb13'
app.register_blueprint(bg)
app.register_blueprint(bp)


app.add_url_rule('/', endpoint='home')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
