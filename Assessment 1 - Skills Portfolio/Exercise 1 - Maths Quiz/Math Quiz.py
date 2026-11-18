from tkinter import *
import random 
import operator


def displayMenu(main_frame):
    main_frame.tkraise()

def easy_diff():
    displayMenu(easy_frame)
def moderate_diff():
    displayMenu(mod_frame)
def advanced_diff():
    displayMenu(adv_frame)

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
easydiff = Button(main_frame, text="Easy", font=('Comfortaa'), width=15, command=easy_diff).pack(pady=10)
moddiff = Button(main_frame, text="Moderate", font=('Comfortaa'), width=15, command=moderate_diff).pack(pady=10)
advdiff = Button(main_frame, text="Advanced", font=('Comfortaa'), width=15, command=advanced_diff).pack(pady=10)

main_frame.place(x=100, y=100, width=400, height=400)  


# Easy Difficulty Frame
easy_frame = Frame(root, bg='pink')
easy_num = Label(easy_frame, text="Easy Difficulty", font=('Comfortaa'), bg='pink').pack()
easy_input = Entry(easy_frame).pack(pady=10)
easy_button = Button(easy_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

easy_frame.place(x=100, y=100, width=400, height=400)


# Moderate Difficulty Frame
mod_frame = Frame(root, bg='pink')
mod_num = Label(mod_frame, text="Moderate Difficulty", font=('Comfortaa'), bg='pink').pack()
mod_input = Entry(mod_frame).pack(pady=10)
mod_button = Button(mod_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

mod_frame.place(x=100, y=100, width=400, height=400)


# Advanced Difficulty Frame
adv_frame = Frame(root, bg='pink')
adv_num = Label(adv_frame, text="Advanced Difficulty", font=('Comfortaa'), bg='pink').pack()
adv_input = Entry(adv_frame).pack(pady=10)
adv_button = Button(adv_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

adv_frame.place(x=100, y=100, width=400, height=400)


displayMenu(main_frame)
root.mainloop()