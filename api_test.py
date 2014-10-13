import json
import urllib2
import requests

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
            print context
            r = main(q)
    jobs = r['jobs']
    for j in jobs:
        print j