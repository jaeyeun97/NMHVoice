from flask import Flask, render_template, redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

app = Flask(__name__)
login_manager = LoginManager(app)
db = SQLAlchemy(app)

from .user import user
app.register_blueprint(user)

from .vote import vote
app.register_blueprint(vote)


@app.route('/')
def index():
    return 'Hello World!'
