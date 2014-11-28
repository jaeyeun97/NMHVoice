from flask import Blueprint
from flask_login import LoginManager

user = Blueprint('user', __name__, template_folder='template', static_folder='static', static_url_path='/user')

import views
