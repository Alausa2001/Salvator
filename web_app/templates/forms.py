from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class SignUpForm(FlaskForm):
    """ SignUpForm : A flaskform instance to generate form using flask """
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField(label="Email address", validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='SIGN UP')