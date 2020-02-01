from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")
    registername = StringField("Full Name", validators=[DataRequired()])
    registeruser = StringField("Register Username", validators=[DataRequired()])
    registerpassword = StringField("Register Full Name", validators=[DataRequired()])
    submitregister = SubmitField("Register")
