from flask import render_template
from flask import redirect
from flask import url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")

def index():
    return redirect("/login")

@app.route("/login")

def login():
    form = LoginForm()
    return render_template("Reggie.html")
