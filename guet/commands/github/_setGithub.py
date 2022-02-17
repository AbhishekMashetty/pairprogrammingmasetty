from typing import List
import urllib.request as http
import json, os, requests

from guet.steps.action import Action

class SetGithub(Action):
    token = os.getenv('GITHUB_TOKEN', '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')
    owner = "AbhishekMashetty"
    repo = "pairprogrammingmasetty"
    query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {
    "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    def __init__(self):
        super().__init__()

    def execute(self, args: List[str]):
        resp = requests.get(SetGithub.query_url, headers=SetGithub.headers, params=SetGithub.params)



