from typing import List
from os.path import join
from pathlib import Path

from guet.committers import CurrentCommitters
from guet.committers.committer import Committer
from guet.git import Git, append_committers
from guet.steps.action import Action
from guet import constants
from guet.config import CONFIGURATION_DIRECTORY
from guet.util import project_root


class CommitMsg(Action):
    def __init__(self, current_committers: CurrentCommitters, git: Git):
        super().__init__()
        self.current_committers = current_committers
        self.git = git

    def execute(self, _):
        new_lines = append_committers(self.current_committers.get(), self.git.commit_msg)
        path = Path(join(CONFIGURATION_DIRECTORY, constants.SESSION_TRACKER))
        project_path = project_root()
        sessionDetails = "No session"
        if path.is_file():
                with open(path) as sessionFile:
                    sessionRecords = sessionFile.readlines()
                for session in sessionRecords:
                    if str(project_path) == session.split(',')[-1].strip("\n\\"):
                        sessionDetails = session.split(',')[0].strip("\n\\")
                        break
        self.git.commit_msg = new_lines + ["Session Details:" + sessionDetails] if sessionDetails else new_lines

    def _co_autor_lines(self, committers: List[Committer]) -> List[str]:
        return [f'Co-authored-by: {committer.name} <{committer.email}>' for committer in committers]
