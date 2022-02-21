from tkinter import *
from guet.commands import CommandMap
from guet.files import FileSystem



class GUI():

    def __init__(self, cMap: CommandMap):
        self.commandMap = cMap
        self.fileSystem = FileSystem()

    def execute(self):
        root = Tk()
        root.geometry('2000x2000')
        #Heading text
        myLabel = Label(root, text="Welcome to guet")
        label2 = Label(root, text="Do pair programming with ease")

        myLabel.grid(row=0, column=0)
        label2.grid(row=2, column=0)


        #Buttons

        button1 = Button(root, text="Init", command=self.guetGUI)
        button1.grid(row=5, column=0)

        button2 = Button(root, text="Yeet", command=self.guetYeet)
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

    
    def guetYeet(self):
        command = self.commandMap.get_command('yeet').build()
        command.play([])

        self.fileSystem.save_all()
    
    def guetGUI(self):
        command = self.commandMap.get_command('init').build()
        command.play([])

        self.fileSystem.save_all()