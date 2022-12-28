from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, FloatField
from wtforms.validators import Length, DataRequired, Email, EqualTo, NumberRange


class LoginForm(FlaskForm):
    """ LoginForm : A flaskform instance to generate login form using flask """
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField(label="Email address", validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label='LOGIN')

    
class SignUpForm(FlaskForm):
    """ SignUpForm : A flaskform instance to generate signup form using flask """
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField(label="Email address", validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='SIGN UP')


class BiodataForm(FlaskForm):
    """ BiodataForm : A flaskform instance to generate Biodata update form """
    firstname = StringField(label='First name', validators=[Length(min=2), DataRequired()])
    lastname = StringField(label='Last name/Surname', validators=[Length(min=2), DataRequired()])
    age = IntegerField(label='Age', validators=[ NumberRange(min=0, max=120), DataRequired()])
    height = FloatField(label='Height', validators=[DataRequired()])
    weight = FloatField(label='Weight', validators=[DataRequired()])
    allergies = StringField(label='Allergies')
    genotype = StringField(label='Genotype', validators=[DataRequired()])
    bloodgroup = StringField(label='Blood Group', validators=[DataRequired()])
    submit = SubmitField(label='Update Biodata')