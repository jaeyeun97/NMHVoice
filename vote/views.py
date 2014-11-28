from flask import render_template, requests, redirect, flash, g
from nmhvoice import db
from nmhvoice.vote import vote

@vote.route('/')
def index():
    return render_template('index.tmpl')
