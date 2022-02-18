from typing import List
from tkinter import *
from guet.steps.action import Action
from guet.commands.init import InitCommandFactory
from guet.git import GitProxy
from guet.files import FileSystem
from guet.commands import CommandMap
from keyboard import press
import os
import appscript


class SetGUI(Action):

    def __init__(self):
        super().__init__()
        self.authToken = ''
        #self.committers = committers
        #self.current_committers = current_committers

    def guetInit():
        #command_map = CommandMap()
        #file_system = FileSystem()

        #os.system('open -a Terminal .')
        appscript.app('Terminal').do_script('guet init')
        #command_map.add_command('gui', InitCommandFactory(
        #GitProxy(), file_system), 'Start guet tracking in the current repository')
        #press('enter')

    def execute(self, args: List[str]):
        
        # lowercase_args = [arg.lower() for arg in args]
        # found = [c for c in self.committers.all() if c.initials in lowercase_args]
        # self.current_committers.set(found)
        # printer = CommittersPrinter(initials_only=False)

        root = Tk()
        #Heading text
        myLabel = Label(root, text="Welcome to guet")
        label2 = Label(root, text="Do pair programming with ease")

        myLabel.grid(row=0, column=0)
        label2.grid(row=2, column=0)

        #Buttons
        button1 = Button(root, text="Initialize guet", command = SetGUI.guetInit)
        button1.grid(row=5, column=0)

        button2 = Button(root, text="Button 2")
        button2.grid(row=6, column=0)

        button3 = Button(root, text="Button 3")
        button3.grid(row=7, column=0)

        button4 = Button(root, text="Button 4")
        button4.grid(row=8, column=0)

        button5 = Button(root, text="Button 5")
        button5.grid(row=9, column=0)

        button6 = Button(root, text="Button 6")
        button6.grid(row=10, column=0)

        #Main loop
        root.mainloop() 