from flask import Flask				# Get some basic Flask tools
from flask.ext.sqlalchemy import SQLAlchemy	# Get the database ORM tools for connecting Flask models to SQL tables

app = Flask(__name__)				# Make an app object
app.config.from_object('config')		# Tell the computer where to get our configuration files
db = SQLAlchemy(app)				# Fire up a database object

from app import views, models			# Pull up the views when the app starts!
