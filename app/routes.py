from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm
from app.backend import addUser
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    registerForm = RegisterForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        login_user(user)
        flash("Login requested for user {}").format(loginForm.username.data)
        return redirect("/")

    #print(registerForm.validate_on_submit())
    if registerForm.validate_on_submit():
        addUser(registerForm.registeruser.data, registerForm.registerpassword.data, registerForm.registername.data)
        flash("Registering")
        return redirect("/")

    return render_template("login.html", form=loginForm, registerform=registerForm)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'

@app.route('/home')
@login_required
def home():

    return 'The curent user is ' + current_user.username