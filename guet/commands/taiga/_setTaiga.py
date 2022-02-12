from typing import List
import urllib.request as http
import json

#from guet.committers import Committers2 as Committers
#from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action


class SetTaiga(Action):
    rootURL = 'https://api.taiga.io/api/v1'
    loginURL = rootURL + '/auth'
    getProjectURL = rootURL + '/projects/by_slug?slug=' # vsingh57-pairprogrammingmasetty
    getSprintsURL = rootURL + '/milestones?project='
    getTasksURL = rootURL + '/tasks'

    def __init__(self):
        super().__init__()
        self.authToken = ''
        #self.committers = committers
        #self.current_committers = current_committers

    def execute(self, args: List[str]):
        # lowercase_args = [arg.lower() for arg in args]
        # found = [c for c in self.committers.all() if c.initials in lowercase_args]
        # self.current_committers.set(found)
        # printer = CommittersPrinter(initials_only=False)

        print('WIP: Taiga tool integration')
        print(args)
        if args[0]=='members':
            user = input('Enter username:')
            pwd = input('Password:')
            self.login(user, pwd)
            slug = input('Project slug:')
            self.getMembers(slug)


    

    def get(self, url):
        req = http.Request(url = url)
        if self.authToken:
            req.add_header("Authorization", "Bearer " + self.authToken)
        with http.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))
            #print(data)
            return data

    def post(self, url, body):
        body = json.dumps(body)
        req = http.Request(url=url, data=bytes(
            body.encode("utf-8")), method="POST")
        req.add_header("Content-type", "application/json; charset=UTF-8") 
        if len(self.authToken): req.add_header("Authorization", "Bearer " + self.authToken)
        with http.urlopen(req) as res:
            data = json.loads(res.read().decode("utf-8"))
            #print(data)
            return data

    def getMembers(self, projectSlug):
        projectData = self.get(self.getProjectURL + projectSlug)
        print('This project has ' + str(len(projectData['members'])) +' members. They are:')
        for person in projectData['members']:
            print(person['full_name'] + ' : ' + person['role_name'])


    def login(self, username, password):
        #f = open('config.json')

        #config = json.load(f)

        data = {
            'username': username,
            'password': password,
            'type': 'normal'
        }
        self.authToken = self.post(self.loginURL, data)['auth_token']
        #f.close() 