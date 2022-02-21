from ctypes import alignment
from tkinter import *
from guet.commands import CommandMap
from guet.files import FileSystem
import os
from guet.commands.add import AddCommandFactory
from guet.commands import CommandMap
from guet.git import GitProxy
from guet.committers import Committers2, CurrentCommitters

class GUI():

    def __init__(self, cMap: CommandMap):
        self.commandMap = cMap
        self.fileSystem = FileSystem()

    def execute(self):
        self.root = Tk()
        self.root.title('GUET')
        self.root.geometry('500x400')
        #Heading text
        #myLabel = Label(self.root, text="Welcome to guet")
        #label2 = Label(self.root, text="Do pair programming with ease")

        #myLabel.grid(row=0, column=0)
        #label2.grid(row=2, column=0)

        self.nav = Frame(self.root, bg='red')
        self.nav.pack(side=LEFT)

        self.view = Frame(self.root, bg='blue')
        self.view.pack(side=RIGHT)

        #Nav Buttons
        button1 = Button(self.root, text="Init", command=self.guetInit, height=2, width=10)
        #button1.grid(row=5, column=0)

        button2 = Button(self.root, text="Yeet", command=self.guetYeet, height=2, width=10)
        #button2.grid(row=10, column=0)

        button3 = Button(self.root, text="Add", height=2, width=10, command=self.buttonAdd)
        #button3.grid(row=6, column=0)

        button4 = Button(self.root, text="Get", height=2, width=10)
        #button4.grid(row=7, column=0)

        button5 = Button(self.root, text="Set", height=2, width=10)
        #button5.grid(row=8, column=0)

        button6 = Button(self.root, text="Remove", height=2, width=10)
        #button6.grid(row=9, column=0)

        label1 = Label(self.view, text='Repository: ' + os.getcwd(), anchor='w')
        label1.pack(side=TOP)
        #label1.grid(row =0, column=30)

        button1.pack(side=TOP, anchor='w')
        button2.pack(side=TOP, anchor='w')
        button3.pack(side=TOP, anchor='w')
        button4.pack(side=TOP, anchor='w')
        button5.pack(side=TOP, anchor='w')
        button6.pack(side=TOP, anchor='w')

        #Main loop
        self.root.mainloop()

    
    def guetYeet(self):
        command = self.commandMap.get_command('yeet').build()
        command.play([])

        self.fileSystem.save_all()
    
    def guetInit(self):
        command = self.commandMap.get_command('init').build()
        command.play([])

        self.fileSystem.save_all()

    def guetAdd(self):
        command = self.commandMap.get_command('add').build()
        command.play([])
        self.fileSystem.save_all()

    def buttonAdd(self):
    
        for widget in self.view.winfo_children():
            widget.destroy()

        newLabel= Label(self.view, text = "Enter Name and email address of the new commiter")
        newLabel.grid(row=1, column=5)
        pName = Entry()
        pEmail = Entry()
        pName.pack()
        pEmail.pack()
        newLabel.pack()