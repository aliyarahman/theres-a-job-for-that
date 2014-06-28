import os
from flask import Flask				# Get some basic Flask tools

app = Flask(__name__)				# Make an app object
app.config.from_object('config')

from app import views				# Pull up the views when the app starts!
