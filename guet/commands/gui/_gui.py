from guet.commands import CommandFactory
from guet.steps import Step
from guet.steps.check import (CommittersExistCheck, GitRequiredCheck,
                              HelpCheck, VersionCheck)
from guet.steps.preparation import InitializePreparation, SwapToLocal
from guet.util import HelpMessageBuilder
from  ._setGUI import SetGUI

class GuiCommandFactory(CommandFactory):
    def __init__(self, file_system, committers, current, git):
        self.committers = committers
        self.current = current
        self.file_system = file_system
        self.git = git

    def build(self) -> Step:
        return VersionCheck() \
            .next(SetGUI()) 
            #.next(CommittersExistCheck(self.committers)) \