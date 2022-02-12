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
        if args[0]=='connect':
        # connect
            self.login(args[1], args[2])
        elif args[0]=='members':
            self.getMembers(args[1])


    

    def get(self, url):
        req = http.Request(url = url)
        if self.authToken:
            f=open('config.json')
            auth = json.load(f)
            if auth["authToken"]:
                req.add_header("Authorization", "Bearer " + auth["authToken"])
            f.close()
        with http.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))
            #print(data)
            return data

    def post(self, url, body):
        f=open('config.json')
        auth = json.load(f)
        body = json.dumps(body)
        req = http.Request(url=url, data=bytes(
            body.encode("utf-8")), method="POST")
        req.add_header("Content-type", "application/json; charset=UTF-8") 
        if len(auth["authToken"]): req.add_header("Authorization", "Bearer " + auth["authToken"])
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
        with open('config.json', 'w') as f:
            json.dump({"authToken": self.authToken}, f )
        #f.close()