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


class SessionTrackerAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        path = Path(join(CONFIGURATION_DIRECTORY, constants.SESSION_TRACKER))
        project_path = project_root()
        sessionExist = False
        if args[0] == 'start':
            print(":::Pair-Programming Session:::")
            timeStamp = datetime.now().strftime("%d-%m-%y-%H:%M:%S")
            sessionDetails = timeStamp + "," + f'{str(project_path)}' + "\n" 
            if path.is_file():
                with open(path) as sessionFile:
                    sessionRecords = sessionFile.readlines()
                for session in sessionRecords:
                    if str(project_path) == session.split(',')[-1].strip("\n\\"):
                        sessionExist = True
                        print("Session Already Exist")
                        break
            if not sessionExist:
                print("New Session started")    
                with path.open('a') as fp:
                    sessionExist = True
                    fp.write(sessionDetails)
        elif args[0] == 'end':
            print(":::Pair-Programming Session:::")
            if path.is_file():
                with open(path,"r") as sessionFile:
                    sessionRecords = sessionFile.readlines()
                with open(path,"w") as sessionFile:
                    for session in sessionRecords:
                        if str(project_path) == session.split(',')[-1].strip("\n\\"):
                            sessionExist = True
                            print("Session Already Exist")
                            print("Session Ended Successfully")
                        else:
                            sessionFile.write(session)
                    if not sessionExist:
                        print("::No seesion found::Cannot End Session::")
        else:
            print("Please pass a valid <identifier>")
            print("For details & help:")
            print("Use: guet session --help")