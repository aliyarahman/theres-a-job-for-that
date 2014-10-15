# -*- coding: utf-8 -*-
import json
import urllib2
import time
import xmltodict
from app import app	# Go get tools we need from the app folder
from flask import render_template, redirect, url_for, session	# So that we can render html files in our app
from .forms import NameForm, LocationForm
import requests	# Allows us to make API calls


def api_call(q):
    url = 'http://174.129.34.133:8080/post'
    data = json.dumps(q)
    clen = len(data)
    req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
    f = urllib2.urlopen(req)
    r = json.load(f)
    f.close()
    return r


@app.route('/', methods=['GET', 'POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect('/location')
    return render_template('login.html', form=form)


@app.route('/location', methods=['GET', 'POST'])
def location():
    form = LocationForm()
    if form.validate_on_submit():
        session['location'] = form.city.data+", "+form.state.data
        return redirect('/start')
    return render_template('location.html', form=form)


@app.route('/start')
def start():
    session['search_string'] ="retail sales"
    session['context']=[]
    return render_template('start.html')


@app.route('/question_view/<swipe>')
def question_view(swipe):
    if swipe=='2':
        q = { "keyword": session['search_string'], "location": session['location'], "context":session['context']}
        r = api_call(q)
        session['question']=r['question']
        return render_template('question.html', question=session['question'])
    else:
        session['context'].append({"question":session['question'], "answer":int(swipe)})
        q = { "keyword": session['search_string'], "location": session['location'], "context":session['context']}
        r = api_call(q)
        if 'jobs' not in r.keys():
            session['question']=r['question']
            return render_template('question.html', question = session['question'])
        else:
        	session['jobs'] = r['jobs']
        	session['job_count'] = r['n_jobs']
        	return redirect(url_for('myjobs'))


@app.route('/matching')
def skills():
	return render_template('matching.html')


@app.route('/myjobs')
def myjobs():
    obj = xmltodict.parse(session['jobs'])
    jobs_obj = obj['rs']['r']
    jobs=[]
    for j in jobs_obj:
        jobs.append({'title':j['jt'],
            'company_url':j['cn'],
            'posting_url':j['src']['@url'],
            'posting_source':j['src']['#text'],
            'location':j['loc']['#text'],
            'date_posted':j['dp'],
            'description':j['e']})
    job_count = len(jobs)
    return render_template('myjobs.html', jobs=jobs, job_count=job_count)