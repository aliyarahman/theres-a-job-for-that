# -*- coding: utf-8 -*-

from app import app	# Go get tools we need from the app folder
from flask import render_template 	# So that we can render html files in our app

@app.route('/')
@app.route('/index')	# This means this is the view for the landing page
def index():
	return "There's a job for that. In development."
