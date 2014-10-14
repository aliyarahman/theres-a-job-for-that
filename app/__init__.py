import os
from flask import Flask, session			# Get some basic Flask tools

app = Flask(__name__)				# Make an app object
app.config.from_object('config')
app.secret_key = 'a394td77fasd98xcvasdfasdf'

from app import views				# Pull up the views when the app starts!
