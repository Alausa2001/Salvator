from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignUpForm(FlaskForm):
    """
    SignUpForm : A flaskform instance to generate form using flask
    """
    username = StringField(label='username')
    password1 = PasswordField(label='password')
    password2 = PasswordField(label='password')
    submit = SubmitField(label='submit')