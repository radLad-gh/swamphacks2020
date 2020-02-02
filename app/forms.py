from flask_wtf import FlaskForm, validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")


class RegisterForm(FlaskForm):
    registername = StringField("Full Name", validators=[DataRequired()])
    registeruser = StringField("Register Username", validators=[DataRequired()])
    registerpassword = PasswordField("Register Full Name", [InputRequired(), EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Repeat Password')
    submitregister = SubmitField("Register")