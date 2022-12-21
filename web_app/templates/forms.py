from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, DecimalField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):
    """
    SignUpForm : A flaskform instance to generate form using flask
    """
    # Personal Details
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    age = DecimalField(label='Age', validators=[DataRequired()])
    height = DecimalField(label='Height (cm)', validators=[DataRequired()])
    weight = DecimalField(label='Weight (kg)', validators=[DataRequired()])
    blood_grp = SelectMultipleField(label='Blood Group ', validators=[DataRequired()])
    genotype = SelectMultipleField(label='Genotype', validators=[DataRequired()])
    # Login Details
    username = StringField(label='Username', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='SIGN UP')

        #   <legend>Medical Records</legend>
        # <label for="datetime">Date and Time</label>
        # <input type="datetime-local" name="datatime">
        # <label for="diagnosis">Diagnosis</label>
        # <textarea name="diagnosis" id="" cols="30" rows="10"></textarea>
        # <label for="prescription">Prescription</label>
        # <textarea name="prescription" id="" cols="30" rows="10"></textarea>
        # <label for="name_of_hospital">Hospital Name</label>
        # <input type="text" name="name_of_hospital">
        # <label for="doctor_name">Doctor's Name</label>
        # <input type="text" name="doctor_name">
        # <label for="doctor_contact">Doctor's Contact</label>
        # <input type="tel" name="doctor_contact">

class LoginForm(FlaskForm):
    """
    LoginForm : A flaskform instance to generate form using flask
    """
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='LOGIN')