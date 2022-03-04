from guet.commands import CommandFactory
from guet.steps import Step
from guet.steps.check import (CommittersExistCheck, GitRequiredCheck,
                              HelpCheck, VersionCheck)
from guet.steps.preparation import InitializePreparation, SwapToLocal
from guet.util import HelpMessageBuilder

from ._setTaiga import SetTaiga

SET_HELP_MESSAGE = HelpMessageBuilder(
    'guet taiga', 'WIP: TOOLS COMMAND').build()


class TaigaCommands(CommandFactory):
    def __init__(self, file_system, committers, current, git):
        self.committers = committers
        self.current = current
        self.file_system = file_system
        self.git = git

    def build(self) -> Step:
        return VersionCheck() \
            .next(HelpCheck(SET_HELP_MESSAGE, stop_on_no_args=True)) \
            .next(InitializePreparation(self.file_system)) \
            .next(GitRequiredCheck(self.git)) \
            .next(SwapToLocal(self.committers)) \
            .next(SetTaiga()) 
            #.next(CommittersExistCheck(self.committers)) \
            
