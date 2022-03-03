from ctypes import alignment
from dataclasses import field
from tkinter import *
from guet.commands import CommandMap
from guet.files import FileSystem
import os
from guet.commands import CommandMap
from guet.git import GitProxy
from guet.committers import Committers2, CurrentCommitters
from guet.commands.set._set_committers import SetCommittersAction
import tkinter.messagebox


class GUI():

    def __init__(self, cMap: CommandMap):
        self.commandMap = cMap
        self.fileSystem = FileSystem()
        self.committers = Committers2(self.fileSystem)
        self.git = GitProxy()
        self.currentCommitters = CurrentCommitters(self.fileSystem, self.committers)
        self.currentCommitters.register_observer(self.git)

    def execute(self):
        self.root = Tk()
        self.root.title('GUET')
        self.root.geometry('600x400')
        #Heading text
        #myLabel = Label(self.root, text="Welcome to guet")
        #label2 = Label(self.root, text="Do pair programming with ease")

        #myLabel.grid(row=0, column=0)
        #label2.grid(row=2, column=0)

        self.nav = Frame(self.root)
        self.nav.pack(side=LEFT)

        self.view = Frame(self.root)
        self.view.pack(side=RIGHT)

        #Nav Buttons
        button1 = Button(self.root, text="Init", command=self.guetInit, height=2, width=10)
        #button1.grid(row=5, column=0)

        button2 = Button(self.root, text="Yeet", command=self.guetYeet, height=2, width=10)
        #button2.grid(row=10, column=0)

        button3 = Button(self.root, text="Add", height=2, width=10, command = self.showAdd)
        #button3.grid(row=6, column=0)

        button4 = Button(self.root, text="Get", height=2, width=10, command=self.showGet)
        #button4.grid(row=7, column=0)

        button5 = Button(self.root, text="Set", height=2, width=10, command = self.showSet)
        #button5.grid(row=8, column=0)

        button6 = Button(self.root, text="Remove", height=2, width=10, command = self.showRemove)
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

    
    def showAlert(self, title, message):
        tkinter.messagebox.showinfo(title,  message)

    
    def guetYeet(self):
        command = self.commandMap.get_command('yeet').build()
        command.play([])
        self.fileSystem.save_all()
        self.showAlert('Remove guet configuration', 'Guet successfully uninstalled from this directory, bye!')
    

    def guetInit(self):        
        command = self.commandMap.get_command('init').build()
        command.play([])
        self.fileSystem.save_all()
        self.showAlert('GUET Initialization', 'Git initialized in this directory')

    def guetAdd(self, inputs):

        initial = inputs[0].get()
        name = inputs[1].get()
        email = inputs[2].get()

        for c in self.committers.all():
            if c.initials == initial:
                self.showAlert("ERROR", "A committer with these initials already exists.")
                return
        
        command = self.commandMap.get_command('add').build()
        command.play([initial, name, email])
        self.fileSystem.save_all()
        self.showAlert('ADD', 'Committer added')
        for textEntry in inputs:
            textEntry.delete(0, END)
        

    def showAdd(self):

        for widget in self.view.winfo_children():
            widget.destroy()

        newLabel = Label(self.view, text = "Enter Initials, Name and email address of the new commiter")
        newLabel.grid(row=1, column=1)

        pInitial = Entry(self.view, borderwidth = 3)
        pName = Entry(self.view, borderwidth = 3)
        pEmail = Entry(self.view, borderwidth = 3)

        self.inputs = [pInitial,pName,pEmail]
        
        initialLabel = Label(self.view, text = "Initial")
        initialLabel.grid(row=3, column=0)

        nameLabel = Label(self.view, text = "Name")
        nameLabel.grid(row=4, column=0)

        emailLabel = Label(self.view, text = "Email")
        emailLabel.grid(row=5, column=0)

        pInitial.grid(row=3, column=1)
        pName.grid(row=4, column=1 )
        pEmail.grid(row=5, column=1)

        button = Button(self.view, text = "Add commiter", height=2, width=10, command = lambda: self.guetAdd([pInitial, pName, pEmail]))
        button.grid(row=7, column=1)

    

    def guetRemove(self, textEntry):

        for c in self.committers.all():
            if c.initials == textEntry.get():
                command = self.commandMap.get_command('remove').build()
                command.play([textEntry.get()])
                self.fileSystem.save_all()
                textEntry.delete(0, END)
                self.showAlert('REMOVE', 'Committer removed successfully.')
                return

        self.showAlert('REMOVE', 'This committer does not exitst')
            

    def showRemove(self):

        for widget in self.view.winfo_children():
            widget.destroy()

        addLabel = Label(self.view, text = "Enter the initials of the programmer you want to remove")
        addLabel.grid(row=1, column=0)

        Initial = Entry(self.view, borderwidth = 3)
        Initial.grid(row=4, column=0)

        button = Button(self.view, text = "Remove", height=2, width=10, command = lambda: self.guetRemove(Initial)) 
        button.grid(row=5, column=0)


    def showGet(self):

        for widget in self.view.winfo_children():
            widget.destroy()

        newLabel = Label(self.view, text = "\t\t\t\t\t\t\t\t")
        newLabel.pack()
        textBox = Text(self.view, state='disabled', height=10, width=40) #, 
        buttonCurrent = Button(self.view, text="get current", height=2, width=10, command=lambda: self.guetGet('current', textBox)) 
        buttonAll = Button(self.view, text="get all", height=2, width=10, command=lambda: self.guetGet('all', textBox))
        buttonCurrent.pack(side=TOP, anchor='n')
        buttonAll.pack(side=TOP, anchor='n')
        textBox.pack()

    def guetGet(self, option, textBox):
        text=''
        if option == 'all':
            cList = self.committers.all()
        elif option == 'current':
            cList = self.currentCommitters.get()
        for c in cList:
            text+=str(c)
            text+='\n'
        textBox.config(state=NORMAL)
        textBox.delete(1.0,"end")
        textBox.insert(1.0, text)
        textBox.config(state=DISABLED)
        self.fileSystem.save_all()

    def showSet(self):
        for widget in self.view.winfo_children():
            widget.destroy()
        
        newLabel = Label(self.view, text = "\t\t\t\t\t\t\t\t")
        newLabel.pack()
        textEntry = Entry(self.view, width=40) 
        textEntry.pack()
        buttonCurrent = Button(self.view, text="Set", height=2, width=10, command=lambda: self.guetSet(textEntry)) 
        buttonCurrent.pack(side=TOP, anchor='n')

    def guetSet(self, textEntry):

        for c in self.committers.all():
            if c.initials == textEntry.get():
                command = self.commandMap.get_command('set').build()
                command.play([textEntry.get()])
                self.fileSystem.save_all()
                textEntry.delete(0, END)
                self.showAlert('REMOVE', 'Committer setsuccessfully.')
                return

        self.showAlert('REMOVE', 'This committer does not exitst')
            