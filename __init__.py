from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
csrf = CsrfProtect(app)


@app.before_first_request
def setup():
    db.create_all()

from nmhvoice.user import user
app.register_blueprint(user)

from nmhvoice.vote import vote
app.register_blueprint(vote, url_prefix='/vote')

@app.route('/')
def index():
    return 'Hello World!'
