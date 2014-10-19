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
        session['job_categories'] = []
        session['jobs'] =[]
        session['context']=[]
        session['all_jobs'] = []
        session['search_strings'] = ['retail sales', 'warehouse worker', 'caregiver', 'data entry']
        session['this_job'] = 'retail sales'
        return render_template('start.html', category=session['this_job'])
    return render_template('location.html', form=form)


@app.route('/start/<category>')
def start(category):
    if category != 'pass':
        session['job_categories'].append(category)
    session['search_strings'].remove(session['this_job'])
    if len(session['search_strings'])>0:
        session['this_job'] = session['search_strings'][0]
        return render_template('start.html', category = session['this_job'])
    else:
        return redirect(url_for('question_view',swipe=2))


@app.route('/question_view/<swipe>')
def question_view(swipe):
    if swipe=='2':
        q = { "keyword": session['job_categories'][0], "location": session['location'], "context":session['context']}
        r = api_call(q)
        session['question']=r['question']
        return render_template('question.html', question=session['question'])
    else:
        session['context'].append({"question":session['question'], "answer":int(swipe)})
        q = { "keyword": session['job_categories'][0], "location": session['location'], "context":session['context']}
        r = api_call(q)
        if 'jobs' not in r.keys():
            session['question']=r['question']
            return render_template('question.html', question = session['question'])
        else:
            obj = xmltodict.parse(r['jobs'])
            jobs_obj = obj['rs']['r']
            for j in jobs_obj:
                description = j['e'][0:-1]
                for i in [['01','January'],['02','February'],['03','March'],['04','April'],['05','May'],['06','June'],['07','July'],['08','August'],['09','September'],['10','October'],['11','November'],['12','December']]:
                    if j['dp'][5:7] == i[0]:
                        month = i[1]
                date_string = month+" "+j['dp'][8:10]+", "+j['dp'][0:4]
                session['all_jobs'].append({'title':j['jt'],'company_url':j['cn'],'posting_url':j['src']['@url'],'posting_source':j['src']['#text'],'location':j['loc']['#text'],'date_posted': date_string,'description':description})
            session['job_categories'].remove(session['job_categories'][0])
            if len(session['job_categories'])==0:
                return redirect(url_for('myjobs'))
            else:
                return redirect(url_for('question_view',swipe=2))


@app.route('/myjobs')
def myjobs(): 
    job_count = len(session['all_jobs'])
    return render_template('myjobs.html', jobs=session['all_jobs'], job_count=job_count)