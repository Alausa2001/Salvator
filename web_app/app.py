from web_app.config import Config
from web_app.auth import bp
from web_app.blog import bg
from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(bg)
app.register_blueprint(bp)

csrf = CSRFProtect(app)

app.add_url_rule('/', endpoint='home')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
