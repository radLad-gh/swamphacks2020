from flask import render_template
from flask import redirect
from flask import url_for
from app import app
from app.forms import LoginForm
import sqlite3


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}").format(form.username.data)
        return redirect("/")
    print()
    print(form.password.data)
    print(form.submit.data)

    return render_template("login.html", form=form)
