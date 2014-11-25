from flask import Blueprint

user = Blueprint('user', __name__, template_folder='template', static_folder='static', static_url_path='/user')

import views