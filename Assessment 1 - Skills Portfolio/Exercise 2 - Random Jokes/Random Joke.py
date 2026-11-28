from tkinter import *
import random


# Open the randomJokes.txt file
with open("randomJokes.txt", "r") as file:
    jokes = file.readlines() # Reads all of the lines of the txt file
    punchline_text = ""

# Makes it so that clicking on the "Tell me a joke" button only generates a joke once
def make_joke():
    if punchline_text == "":
        next_joke()

# When the 'Next Joke' button is pressed it continues to generate more jokes from the file 
def next_joke():
    global punchline_text
    tell_joke = random.choice(jokes) # Randomizes the jokes in the txt file
    line = tell_joke.strip().split("?", 1) # Splits the jokes from the punchline from the question mark symbol
    joke.config(text=line[0] + "?")
    punchline_text = line[1]
    punchline.config(text="")

# Calls the last function because the punchline is split from the joke 
def show_punchline():
    punchline.config(text=punchline_text)


root = Tk()
root.title('Random Jokes')
root.config(bg='pink')
root.geometry('750x500')
root.resizable(0,0)

    
# Main Screen
main_screen = Frame(root, bg="pink")
joke = Label(main_screen, text='', font=('Comfortaa'), bg='pink', width=50)
joke.grid(row=0, column=0, columnspan=2, pady=5)
punchline = Label(main_screen, text='', font=('Comfortaa'), bg='pink', width=50)
punchline.grid(row=1, column=0, columnspan=2, pady=25)
# Buttons for jokes and a quit button to exit the window
display_joke = Button(main_screen, text='Tell me a joke', font=('Comfortaa'), width=20, command=make_joke).grid(row=2, column=0, padx=5, pady=20)
punchline_button = Button(main_screen, text='Show Punchline', font=('Comfortaa'), width=20, command=show_punchline).grid(row=2, column=1, pady=5, padx=20)
next_button = Button(main_screen, text='Next Joke', font=('Comfortaa'), width=20, command=next_joke).grid(row=3, column=0, padx=5, pady=10)
quit_button = Button(main_screen, text='Quit', font=('Comfortaa'), width=20, command=root.destroy).grid(row=3, column=1, padx=5, pady=10)

# Fixes the position of the whole frame on the window
main_screen.place(x=110, y=100, width=600, height=400)


root.mainloop()