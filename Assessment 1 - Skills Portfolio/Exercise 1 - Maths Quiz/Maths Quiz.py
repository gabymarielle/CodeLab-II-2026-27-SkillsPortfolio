from tkinter import *
import random
import operator 

# Function to switch the frames
def switch_frame(frame):
    frame.tkraise()

def easy_diff():
    switch_frame(frame2)
def moderate_diff():
    switch_frame(frame3)
def advanced_diff():
    switch_frame(frame4)

#operation = ['+', '-']
def decideOperation():
    operation = ['+', '-']
    value = random.choice(operation)
    return value

#flow: randomizer -> return

easynum = random.randint(0,9)
moderatenum = random.randint(10,99)


def randomInt():
    if easynum:
        print(f"Question: {easynum}{oper_value}{easynum}")
    elif moderatenum == random.randint(10, 99):
        print('{moderatenum}{oper_value}{moderatenum}')
    return

oper_value =  decideOperation()

# Creates the window of the GUI
root = Tk()
root.title('Math Quiz')
root.config(bg='pink')
root.geometry('600x600')
root.resizable(0,0)

# Frame 1 - Includes the introduction to the quiz and where you can choose the difficulty of the quiz
frame1 = Frame(root, bg="pink")

label1 = Label(frame1, text="Welcome to Gaby's Math Quiz")
label1.pack()
label2 = Label(frame1, text="Test out your skills in this quiz!")
label2.pack()

diff = Label(frame1, text="Choose your difficulty level:")
diff.pack()
# Buttons to direct to a different frame of your chosen difficulty
button1 = Button(frame1, text="Easy", command=easy_diff)
button1.pack()
button2 = Button(frame1, text="Moderate", command=moderate_diff)
button2.pack()
button3 = Button(frame1, text="Advanced", command=advanced_diff)
button3.pack()
 
frame1.place(x=95,y=50, width=400,height=400)

# Frame 2 - Easy difficulty page
frame2 = Frame(root, bg="pink") 

label3 = Label(frame2, text="Easy difficulty")
label3.pack()

easynum = Label(frame2, text=f"Question: {easynum}{oper_value}{easynum}")
#temp_easy = (values from question) - use for comparing the value with the user's input
easynum.pack()


# An entry function to submit your answers
entry1 = Entry(frame2)
entry1.pack()

button4 = Button(frame2, text="Submit")
button4.pack()
backb = Button(frame2, text="Go Back", command=lambda: switch_frame(frame1))
backb.pack()

frame2.place(x=95,y=50, width=400,height=400)

# Frame 3 - Moderate difficulty page
frame3 = Frame(root, bg="pink")

label4 = Label(frame3, text="Moderate difficulty")
label4.pack()

moderatenum = Label(frame3, text=f"Question: {randomInt}")
moderatenum.pack()


#question - randomnum1 + operator + randomnum2

entry2 = Entry(frame3)
entry2.pack()

button5 = Button(frame3, text="Submit")
button5.pack()
backb2 = Button(frame3, text="Go Back", command=lambda: switch_frame(frame1))
backb2.pack()

frame3.place(x=95,y=50, width=400,height=400)

# Frame 4 - Advanced difficulty page
frame4 = Frame(root, bg="pink")

label5 = Label(frame4, text="Advanced difficulty")
label5.pack()

random_num3 = random.randint(1000, 9999)
advancednum = Label(frame4, text=f"Question: {random_num3}")
advancednum.pack()

entry3 = Entry(frame4)
entry3.pack()

button6 = Button(frame4, text="Submit")
button6.pack()
backb3 = Button(frame4, text="Go Back", command=lambda: switch_frame(frame1))
backb3.pack()

frame4.place(x=95,y=50, width=400,height=400)


switch_frame(frame1)
root.mainloop()