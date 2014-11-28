import sys, os
sys.path.append(os.getcwd())
from nmhvoice import app

print os.getcwd()
app.run(debug=True)
