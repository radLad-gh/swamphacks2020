import os

class Config(self):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
