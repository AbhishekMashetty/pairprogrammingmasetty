from typing import List
import requests, json
from guet.steps.action import Action


class RemoveCommitterAction(Action):
    def __init__(self, committers):
        super().__init__()
        self.committers = committers

    def execute(self, args: List[str]):
        committer = self.committers.by_initials(args[0])
        headers = {'Content-type': 'application/json',}
        if not committer:
            print(f'No committer exists with initials {args[0]}')
        else:
            message = args[0]+" is removed as a committer"
            temp = {"text": message}
            data = json.dumps(temp)
            with open('PATH TO THE FILE WHICH HAS WEBHOOK OF SLACK CHANNEL', 'r') as f:
                url = json.loads(f.read())
            requests.post(url["URL"], headers=headers, data=data)
            self.committers.remove(committer.initials)

