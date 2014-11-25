from flask import Blueprint

vote = Blueprint('vote',__name__,template_folder='templates',static_url_path='/vote',static_folder='static')

import views