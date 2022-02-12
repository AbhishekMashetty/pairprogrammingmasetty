from tkinter import *

root = Tk()
#Heading text
myLabel = Label(root, text="Welcome to guet")
label2 = Label(root, text="Do pair programming with ease")

myLabel.grid(row=0, column=0)
label2.grid(row=2, column=0)


#Buttons
button1 = Button(root, text="Button 1")
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