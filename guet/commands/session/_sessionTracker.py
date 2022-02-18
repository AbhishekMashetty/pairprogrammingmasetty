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

    # def new_timestamp():
    #     # Creates a new timestamp with a specific format.
    #     return datetime.now().strftime("%d/%m/%y - %H:%M:%S")

    def execute(self, args: List[str]):

        if args[0] == 'start':
            print(":::Pair-Programming Session Starts:::")
            path = Path(join(CONFIGURATION_DIRECTORY, constants.SESSION_TRACKER))
            project_path = project_root()
            timeStamp = datetime.now().strftime("%d-%m-%y-%H:%M:%S")
            sessionDetails = timeStamp + "," + f'{project_path}\n'
            sessionExist = False
            print(project_path)
            if path.is_file():
                with open(path) as sessionFile:
                    sessionRecords = sessionFile.readlines()
                for session in sessionRecords:
                    if project_path == session.split(',')[-1]:
                        sessionExist = True
                        print("Session Already Exist")
            if not sessionExist:    
                with path.open('a') as fp:
                    sessionExist = True
                    fp.write(sessionDetails)
            #path.write_text(sessionDetails)
            #write_lines(path, timeStamp + "," + f'{project_path}')
            # committers = self.committers.all()
            # pre_print = 'All committers'
        elif args[0] == 'end':
            print(":::Pair-Programming Session Ends:::")
            # committers = self.current.get()
            # pre_print = 'Current committers'
        else:
            print("Please pass a valid <identifier>")
            print("For details & help:")
            print("Use: guet session --help")

    
        


# class GetCommittersAction(Action):

#     def execute(self, args: List[str]):
#         printer = CommittersPrinter(initials_only=False)
#         if args[0] == 'all':
#             committers = self.committers.all()
#             pre_print = 'All committers'
#         else:
#             committers = self.current.get()
#             pre_print = 'Current committers'

#         print(pre_print)
#         printer.print(committers)

#         lowercase_args = [arg.lower() for arg in args]
#         initialsList = {}
#         for c in self.committers.all():
#             initialsList[c.initials] = c
#         found = []
#         #allCommitters = self.committers.all()
#         for arg in lowercase_args:
#             if arg in initialsList:
#                 found.append(initialsList[arg])        
#                 #for c in allCommitters:
#                 #    if c.initials == arg:
#                 #        found.append(c)
#         #found = [c for c in self.committers.all() if c.initials in lowercase_args]
#         driver = found[0]
#         observers = found[1:]
#         observers.sort(key=lambda x: x.initials)
#         found = [driver]
#         for obs in observers:
#             found.append(obs)
#         self.current_committers.set(found)
#         printer = CommittersPrinter(initials_only=False)
#         print('Committers set to:')
#         printer.print(found)