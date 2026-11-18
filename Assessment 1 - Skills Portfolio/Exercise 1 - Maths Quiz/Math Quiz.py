from tkinter import *
import random 
import operator


def displayMenu():
    main_frame.tkraise()

#def randomInt():
    #if difficulty 

#def decideOperation():

#def displayProblem():

#def displayResults():




root = Tk()
root.title('Math Quiz')
root.config(bg='pink')
root.geometry('600x600')
root.resizable(0,0)

# Main Menu Frame 
main_frame = Frame(root, bg='pink')
label1 = Label(main_frame, text="Welcome to Gaby's Math Quiz", font=('Comfortaa'), bg='pink').pack()
label2 = Label(main_frame, text="Test out your skills in this quiz!", font=('Comfortaa'), bg='pink').pack()
diff = Label(main_frame, text="Choose your difficulty:", font=('Comfortaa'), bg='pink').pack(pady=20)
easydiff = Button(main_frame, text="Easy", font=('Comfortaa'), width=15).pack(pady=10)
moddiff = Button(main_frame, text="Moderate", font=('Comfortaa'), width=15).pack(pady=10)
advdiff = Button(main_frame, text="Advanced", font=('Comfortaa'), width=15).pack(pady=10)

main_frame.place(x=100, y=100, width=400, height=400)    

root.mainloop()