import time
from os.path import join
from pathlib import Path
from typing import List
from datetime import datetime, timedelta

from guet import constants
from guet.committers import Committers2 as Committers
from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action
from guet.config import CONFIGURATION_DIRECTORY
from guet.files.write_lines import write_lines
from guet.files import FileSystem
from guet.util import project_root


class DeveloperKarmaAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        print("#####Developer Karma Display#####")
        