from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCUEMY_DATABASE_URI'] = 'sqlite:////Users/michel/Desktop/swamphacks2020/app/backend/userDatabase.sqlite'
app.config['SECRET_KEY'] = "you-will-never-guess"

from app import routes
