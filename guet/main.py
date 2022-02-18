import sys
from tkinter import *
from guet.commands import CommandMap
from guet.commands.add import AddCommandFactory
from guet.commands.get import GetCommandFactory
from guet.commands.help import HelpCommandFactory, UnknownCommandFactory
from guet.commands.init import InitCommandFactory
from guet.commands.remove import RemoveCommandFactory
from guet.commands.set import SetCommittersCommand
from guet.commands.yeet import YeetCommandFactory
from guet.commands.taiga import TaigaCommands
from guet.commands.session import SessionCommandFactory
from guet.commands.github import GithubCommands
from guet.committers import Committers2, CurrentCommitters
from guet.files import FileSystem
from guet.git import GitProxy
from guet.util import add_command_help_if_invalid_command_given
from guet.util.errors import log_on_error

from guet.UI import GUI

@log_on_error
def main():
    file_system = FileSystem()
    committers = Committers2(file_system)
    git = GitProxy()
    current_committers = CurrentCommitters(file_system, committers)
    current_committers.register_observer(git)

    command_map = CommandMap()
    command_map.add_command('help', HelpCommandFactory(
        command_map, file_system), 'Display guet usage')
    command_map.add_command('init', InitCommandFactory(
        GitProxy(), file_system), 'Start guet tracking in the current repository')
    command_map.add_command('add', AddCommandFactory(
        file_system, committers, git), 'Add committer for tracking')
    command_map.add_command('get', GetCommandFactory(
        file_system, committers, current_committers), 'List information about committers')
    command_map.add_command('set', SetCommittersCommand(
        file_system, committers, current_committers, git), 'Set committers for current repository')
    command_map.add_command('remove', RemoveCommandFactory(
        file_system, committers), 'Remove committer')
    command_map.add_command('taiga', TaigaCommands(
        file_system, committers, current_committers, git), 'Integrate taiga')
    command_map.add_command('session', SessionCommandFactory(
        file_system, committers, current_committers, git), 'Pair-Programming Session Tracker')  
    command_map.add_command('github', GithubCommands(
        file_system, committers, current_committers, git), 'Get Issues from github')
    command_map.add_command('yeet',
                            YeetCommandFactory(file_system, git),
                            'Remove guet configurations')


    command_map.set_default(UnknownCommandFactory(command_map))

    args = add_command_help_if_invalid_command_given(sys.argv[1:])

    if args[0]=='gui':
        print('UI opens here')
        interface = GUI(command_map)
        interface.execute()
    else:
        command = command_map.get_command(args[0]).build()
        command.play(args[1:])

        file_system.save_all()

