from tkinter import *

# Function to switch the frames
def switch_frame(frame):
    frame.tkraise()

def easy_difficulty():
    switch_frame(frame2)

# Creates the window of the GUI
root = Tk()
root.title('Maths Quiz')
root.config(bg='pink')
root.geometry('600x600')
root.resizable(0,0)

# Frame 1 - Includes the introduction to the quiz and where you can choose the difficulty of the quiz
frame1 = Frame(root, bg="pink")

greeting = Label(frame1, text="Welcome to Gaby's Math Quiz")
greeting.pack()
greeting2 = Label(frame1, text="Test out your skills in this quiz!")
greeting2.pack()

diff = Label(frame1, text="Choose your difficulty level:")
diff.pack()
button1 = Button(frame1, text="Easy", command=lambda: switch_frame(frame2))
button1.pack()
Button(frame1, text="Moderate").pack()
Button(frame1, text="Advanced").pack()

frame1.place(x=95,y=50, width=400,height=400)

# Frame 2 - Easy difficulty page
frame2 = Frame(root, bg="pink")

label2 = Label(frame2, text="Easy difficulty")
label2.pack()

entry1 = Entry(frame2)
entry1.pack()

button4 = Button(frame2, text="Submit")
button4.pack()

frame2.place(x=95,y=50, width=400,height=400)



switch_frame(frame1)
root.mainloop()