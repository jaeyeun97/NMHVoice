# This is a config file for the NMH Voice Project.
import random, string
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = ''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])
WTF_CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DEBUG=True
