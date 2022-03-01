from typing import List
import urllib.request as http
import json, requests
from guet.steps.action import Action
from guet.commands.add import _add_committer
from guet.files import FileSystem
from guet.commands import CommandMap
from guet.committers import Committers2, CurrentCommitters
from guet.committers.committer import Committer


class SetTaiga(Action):
    rootURL = 'https://api.taiga.io/api/v1'
    loginURL = rootURL + '/auth'
    getProjectURL = rootURL + '/projects/by_slug?slug=' # vsingh57-pairprogrammingmasetty
    getSprintsURL = rootURL + '/milestones?project='
    getTasksURL = rootURL + '/tasks'

    def __init__(self):
        super().__init__()
        self.authToken = ''
        file_system = FileSystem()
        committers = Committers2(file_system)

    def execute(self, args: List[str]):
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
            return data

    def post(self, url, body):
        body = json.dumps(body)
        req = http.Request(url=url, data=bytes(
            body.encode("utf-8")), method="POST")
        req.add_header("Content-type", "application/json; charset=UTF-8") 
        if len(self.authToken): req.add_header("Authorization", "Bearer " + self.authToken)
        with http.urlopen(req) as res:
            data = json.loads(res.read().decode("utf-8"))
            return data

    def getMembers(self, projectSlug):
        memberData=[]
        userNames = []
        projectData = self.get(self.getProjectURL + projectSlug)
        print('This project has ' + str(len(projectData['members'])) +' members. They are:')
        for person in projectData['members']:
            userNames.append(person["username"])
        for person in projectData['members']:
            print(person['full_name'] + ' : ' + person['role_name'])
        flag = input("Do you want to save the team members as committers? (Y/N): ")
        if flag == 'Y' or flag == 'y':
            email=[]
            for person in projectData['members']:
                memberData.append(person['full_name'])
            for i in userNames:
                email.append(i+"@asu.edu")
        self.saveCommitters(userNames, email)
        return memberData
    
    def saveCommitters(self, firstNames, emails):
        filesystem = FileSystem()
        committers = Committers2(filesystem)
        firstNames=firstNames
        emails=emails
        initials = []
        for i in firstNames:
            initials.append(i[0:2]+"1")
        for i in range(len(firstNames)):
            committer = Committer(firstNames[i], emails[i], initials[i])
            committer = committers.add(committer)
        print("All the taiga members are set as committers. Check using guet get all command")
        
    def login(self, username, password):
        data = {
            'username': username,
            'password': password,
            'type': 'normal'
        }
        self.authToken = self.post(self.loginURL, data)['auth_token']