from guet.commands import CommandFactory
from guet.committers import Committers2 as Committers
from guet.committers import CurrentCommitters
from guet.files import FileSystem
from guet.steps import Step
from guet.steps.check import (CommittersExistCheck, GitRequiredCheck, HelpCheck, VersionCheck)
from guet.steps.preparation import InitializePreparation, SwapToLocal
from guet.util import HelpMessageBuilder

from ._action import DeveloperKarmaAction

DK_HELP_MESSAGE = HelpMessageBuilder('guet developerkarma',
                                      'Display aggregated contributions from each developer.') \
    .explanation(('No Identifier\n\tDo not enter any identifier')) \
    .build()


class DeveloperKarmaCommandFactory(CommandFactory):
    def __init__(self,
                 file_system: FileSystem,
                 committers: Committers,
                 current_committers: CurrentCommitters,
                 git):

        self.file_system = file_system
        self.committers = committers
        self.current = current_committers
        self.git = git

    def build(self) -> Step:
        return VersionCheck() \
            .next(HelpCheck(DK_HELP_MESSAGE, stop_on_no_args=False)) \
            .next(InitializePreparation(self.file_system)) \
            .next(GitRequiredCheck(self.git)) \
            .next(SwapToLocal(self.committers)) \
            .next(DeveloperKarmaAction(self.committers, self.current))
