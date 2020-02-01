from flask import render_template
from app import app


@app.route("/")
@app.route("/index")

def index():
    user = {"username": "Mahan"}
    return render_template("index.html", name="home", user=user)
