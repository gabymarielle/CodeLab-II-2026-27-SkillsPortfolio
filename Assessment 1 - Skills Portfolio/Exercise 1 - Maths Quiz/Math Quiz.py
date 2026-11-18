from tkinter import *
import random 
import operator

def displayMenu(main_frame):
    main_frame.tkraise()

#redefine with actual values
def easy_diff():
    displayMenu(easy_frame)
def moderate_diff():
    displayMenu(mod_frame)
def advanced_diff():
    displayMenu(adv_frame)

var1 = 0
var2 = 0

#required function
def decideOperation():
    operation = ['+', '-']
    symbol = random.choice(operation)
    return symbol

#required function
def displayProblem(var1, var2):
    oper = decideOperation()
    question = f"{var1} {oper} {var2}"
    return question

#required function
def randomInt(difficulty):
    if difficulty == 'easy':
        var1 = random.randint(0, 9)
        var2 = random.randint(0, 9)
        return var1, var2
    elif difficulty == 'moderate':
        var1 = random.randint(10, 99)
        var2 = random.randint(10, 99)
        return var1, var2
    elif difficulty == 'advanced':
        var1 = random.randint(1000, 9999)
        var2 = random.randint(1000, 9999)
        return var1, var2

def askQuestion(difficulty):
    testType = difficulty
    rand1, rand2 = randomInt(testType)
    return displayProblem(rand1, rand2)
    answer = eval(question)



#ops = {'+': operator.add,
       #'-': operator.sub}

#def decideOperation():
    #value = random.choice(list(ops.keys()))
    #return value





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
easy_question = Label(easy_frame, text=f"{askQuestion('easy')}").pack()    
easy_input = Entry(easy_frame).pack(pady=10)
easy_button = Button(easy_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

easy_frame.place(x=100, y=100, width=400, height=400)


# Moderate Difficulty Frame
mod_frame = Frame(root, bg='pink')
mod_num = Label(mod_frame, text="Moderate Difficulty", font=('Comfortaa'), bg='pink').pack()
mod_question = Label(mod_frame, text=f"{askQuestion('moderate')}").pack()
mod_input = Entry(mod_frame).pack(pady=10)
mod_button = Button(mod_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

mod_frame.place(x=100, y=100, width=400, height=400)


# Advanced Difficulty Frame
adv_frame = Frame(root, bg='pink')
adv_num = Label(adv_frame, text="Advanced Difficulty", font=('Comfortaa'), bg='pink').pack()
adv_question = Label(adv_frame, text=f"{askQuestion('advanced')}").pack()
adv_input = Entry(adv_frame).pack(pady=10)
adv_button = Button(adv_frame, text="Submit", font=('Comfortaa')).pack(pady=10)

adv_frame.place(x=100, y=100, width=400, height=400)



displayMenu(main_frame)
root.mainloop()