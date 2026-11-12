from tkinter import *

# Creates the window of the GUI
root = Tk()
root.title('Maths Quiz')
root.geometry('350x600')

greeting = Label(root, text="Welcome to Gaby's Math Quiz")
greeting.pack()
greeting2 = Label(root, text="Test out your skills in this quiz!")
greeting2.pack()

diff = Label(root, text="Choose your difficulty level:")
diff.pack()
Button(root, text="Easy").pack()
Button(root, text="Moderate").pack()
Button(root, text="Advanced").pack()



root.mainloop()