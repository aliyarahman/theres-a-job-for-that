# -*- coding: utf-8 -*-

import random
from app import app	# Go get tools we need from the app folder
from flask import render_template, redirect 	# So that we can render html files in our app

@app.route('/')
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/index')	# This means this is the view for the landing page
def index():
	return render_template('index.html')

# Question screen views follow - once we get a database connection we can probably collapse these into one view
# and query be category on the homepage button click (e.g. they click "I Can" and it passes "can" as category
# into db query

@app.route('/i_can/<can_counter>')
def i_can(can_counter):
	counter=int(can_counter)
	if counter==3:
		return redirect('index')
	counter+=1
	can_questions = ['I can drive a car', 'I can speak Spanish', 'I can fix a carburetor', 'I can plant a tree']
	can_question = can_questions[counter]
	return render_template('can_question.html', question=can_question, can_counter=counter)

@app.route('/i_want/<want_counter>')
def i_want(want_counter):
	counter=int(want_counter)
	if counter==3:
		return redirect('index')
	counter+=1
	want_questions = ['I want to work outdoors', 'I want to work on a team','I want to work with seniors', 'I want to learn new skills']
	want_question = want_questions[counter]
	return render_template('want_question.html', question=want_question, want_counter=counter)

@app.route('/i_need/<need_counter>')
def i_need(need_counter):
	counter=int(need_counter)
	if counter==3:
		return redirect('matching')
	counter+=1
	need_questions = ['I need flexible work hours', 'I need trans inclusive health care', 'I need a veteran friendly employer', 'I need an employer who hires people with criminal records']
	need_question = need_questions[counter]
	return render_template('need_question.html', question=need_question, need_counter= counter)


# Notification of skill language generated
@app.route('/matching')
def skills():
	return render_template('matching.html')


# Displays calculated list of jobs (after algorithm)
@app.route('/myjobs')
def myjobs():
	jobs = [{'id':1, 'title':'Tool and die maker'}, {'id':2,'title':'Home care professional'}, {'id':3,'title':'Park ranger'}, {'id':4,'title':'Underwater welder'}, {'id':5,'title':'Greenhouse manager'},{'id':6,'title':'Automobile mechanic'},{'id':7,'title':'Roofer'},{'id':8,'title':'Admin assistant'},{'id':9,'title':'Forklift operator'}] 
	return render_template('myjobs.html', jobs=jobs)


@app.route('/jobView/<id>')
def jobView(id):
	jobs = [{'id':1, 'title':'Tool and die maker'}, {'id':2,'title':'Home care professional'}, {'id':3,'title':'Park ranger'}, {'id':4,'title':'Underwater welder'}, {'id':5,'title':'Greenhouse manager'},{'id':6,'title':'Automobile mechanic'},{'id':7,'title':'Roofer'},{'id':8,'title':'Admin assistant'},{'id':9,'title':'Forklift operator'}] 
	for j in jobs:
		if j['id']==int(id):
			job=j
	return render_template('jobView.html', job=job)
