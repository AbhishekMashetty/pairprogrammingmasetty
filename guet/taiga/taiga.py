import urllib.request as http
import json
import datetime

rootURL = 'https://api.taiga.io/api/v1'
loginURL = rootURL + '/auth'
getProjectURL = rootURL + '/projects/by_slug?slug='
getSprintsURL = rootURL + '/milestones?project='
getTasksURL = rootURL + '/tasks'

authToken = None

def get(url):
    req = http.Request(url = url)
    if authToken:
        req.add_header("Authorization", "Bearer " + authToken)
    with http.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        #print(data)
        return data

def post(url, body):
    body = json.dumps(body)
    req = http.Request(url=url, data=bytes(
        body.encode("utf-8")), method="POST")
    req.add_header("Content-type", "application/json; charset=UTF-8")
    if authToken:
        req.add_header("Authorization", "Bearer " + authToken)
    with http.urlopen(req) as res:
        data = json.loads(res.read().decode("utf-8"))
        #print(data)
        return data

def login():
    f = open('config.json')
 
    # returns JSON object as
    # a dictionary
    config = json.load(f)

    data = {
        'username': config['taiga']['username'],
        'password': config['taiga']['password'],
        'type': 'normal'
    }
    global authToken
    authToken = post(loginURL, data)['auth_token']
    f.close()


def getTeamMembers():
    login()
    f=open('config.json')
    config = json.load(f)
    projectData = get(getProjectURL + config['taiga']['projectSlug'])
    print('This project has ' + str(len(projectData['members'])) +' members. They are:')
    for person in projectData['members']:
        print(person['full_name'] + ' : ' + person['role_name'])
