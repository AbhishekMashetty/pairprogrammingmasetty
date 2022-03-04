from itertools import count
import subprocess
import sys

from pathlib import Path
from typing import List
from collections import Counter

from guet import constants
from guet.committers import Committers2 as Committers
from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action
from guet.util import project_root


class DeveloperKarmaAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        package = 'GitPython'
        import importlib
        try:
            importlib.import_module('git')
            print(package + '- Package already exists')
        except ImportError:
            subprocess.check_call([sys.executable,'-m','pip','install',package])
        finally:
            globals()[package] = importlib.import_module('git')
            print('git ' + ' Package Imported')

        import git
        print("#####Developer Karma Display#####")
        path = Path(str(project_root()))
        repo = git.Repo(path)
        commits = list(repo.iter_commits("main"))
        committers = []
        for commit in commits:
            committers.append(commit.author)
        developerKarma = Counter(committers)
        print("Aggregated Contributions from each committer to main branch")
        print("Committer:Commits")
        for sign, count in developerKarma.most_common():
            print(str(sign) + ":" + str(count))
