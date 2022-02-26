from typing import List
import urllib.request as http
import json, os, requests

from guet.steps.action import Action

class SetGithub(Action):
    token = os.getenv('GITHUB_TOKEN', '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')
    owner = "AbhishekMashetty"
    repo = "assign-git"
    query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {
    "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    def __init__(self):
        super().__init__()

    def execute(self, args: List[str]):
        if args[0]=="issues":
            token = input("Enter the token:")
            owner = input("Enter the repo owner name:")
            repo = input("Enter the repository name:")
            query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
            params = {
            "state": "open",
            }
            headers = {'Authorization': f'token {token}'}
            print(self.getdata())
        else:
            print("Invalid Command")

    def getdata(self):
        resp = requests.get(SetGithub.query_url, headers=SetGithub.headers, params=SetGithub.params)
        output = resp.json()
        output_map = {}
        for i in output:
            for key,val in i.items():
                output_map[i["title"]] = i["body"]
        
        for key in output_map:
            print("#Issue number: ",key, "\n", output_map[key])