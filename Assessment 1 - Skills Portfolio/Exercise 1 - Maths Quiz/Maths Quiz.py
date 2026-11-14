from tkinter import *

# Function to switch the frames
def switch_frame(frame):
    frame.tkraise()

def easy_diff():
    switch_frame(frame2)

# Creates the window of the GUI
root = Tk()
root.title('Maths Quiz')
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
button1 = Button(frame1, text="Easy", command=lambda: switch_frame(frame2))
button1.pack()
button2 = Button(frame1, text="Moderate", command=lambda: switch_frame(frame3))
button2.pack()
button3 = Button(frame1, text="Advanced", command=lambda: switch_frame())
button3.pack()

frame1.place(x=95,y=50, width=400,height=400)

# Frame 2 - Easy difficulty page
frame2 = Frame(root, bg="pink") 

label3 = Label(frame2, text="Easy difficulty")
label3.pack()

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

entry2 = Entry(frame3)
entry2.pack()

button5 = Button(frame3, text="Submit")
button5.pack()
backb2 = Button(frame3, text="Go Back", command=lambda: switch_frame(frame1))
backb2.pack()

frame2.place(x=95,y=50, width=400,height=400)


switch_frame(frame1)
root.mainloop()