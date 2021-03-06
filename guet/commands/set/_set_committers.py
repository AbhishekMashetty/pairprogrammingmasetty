from typing import List

from guet.committers import Committers2 as Committers
from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action


class SetCommittersAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        lowercase_args = [arg.lower() for arg in args]
        initialsList = {}
        for c in self.committers.all():
            initialsList[c.initials] = c
        found = []
        #allCommitters = self.committers.all()
        for arg in lowercase_args:
            if arg in initialsList:
                found.append(initialsList[arg])        
                #for c in allCommitters:
                #    if c.initials == arg:
                #        found.append(c)
        #found = [c for c in self.committers.all() if c.initials in lowercase_args]
        driver = found[0]
        observers = found[1:]
        observers.sort(key=lambda x: x.initials)
        found = [driver]
        for obs in observers:
            found.append(obs)
        self.current_committers.set(found)
        printer = CommittersPrinter(initials_only=False)
        print('Committers set to:')
        printer.print(found)
