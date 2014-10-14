import json
import urllib2
import requests
import pprint
import xmltodict

url = 'http://174.129.34.133:8080/post'

def main(q):
        data = json.dumps(q)
        clen = len(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
        f = urllib2.urlopen(req)
        r = json.load(f)
        f.close()
        return r

if __name__ == '__main__':
    location = "Waterloo, IA"
    search_string ="retail sales"
    context = []
    q = { "keyword": search_string, "location": location, "context":context}
    r = main(q)
    while 'jobs' not in r.keys():
        question = r['question']
        answer = input(question+": ")
        if answer in [0,1]:
            context.append({"question":r['question'], "answer":answer})
            r = main(q)
    obj = xmltodict.parse(r['jobs'])
    jobs = obj['rs']['r']
    ''' print jobs[0]['jt'] #Job title
    print jobs[0]['cn'] # Company URL
    print jobs[0]['src']['@url'] #Link to posting URL
    print jobs[0]['src']['#text'] #Job link source
    print jobs[0]['ty'] # Type? May not be of use.
    print jobs[0]['loc']['@cty'] # City
    print jobs[0]['loc']['@st'] # State
    print jobs[0]['loc']['@postal'] # Zip code
    print jobs[0]['loc']['@county'] # County
    print jobs[0]['loc']['@region'] # Region (empty in many cases)
    print jobs[0]['loc']['@country'] # Country
    print jobs[0]['loc']['#text'] # String of text to use (city and state in most cases)
    print jobs[0]['ls'] # ?
    print jobs[0]['dp'] # When posted
    print jobs[0]['e'] # Description of responsibility'''