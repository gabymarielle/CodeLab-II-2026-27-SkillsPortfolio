from tkinter import *
import random


root = Tk()
root.title('Random Jokes')
root.config(bg='pink')
root.geometry('750x500')
root.resizable(0,0)

# Open the randomJokes.txt file
with open("randomJokes.txt", "r", encoding='utf-8') as file:
    jokes = file.readlines()
    punchline_text = ""

def make_joke():
    global punchline_text
    tell_joke = random.choice(jokes)
    line = tell_joke.strip().split("?", 1)
    joke.config(text=line[0] + "?")
    punchline_text = line[1]
    punchline.config(text="")


    
# Main Screen
main_screen = Frame(root, bg="pink")
joke = Label(main_screen, text='', font=('Comfortaa'), bg='pink', width=50)
joke.grid(row=0, column=0, columnspan=2, pady=5)
punchline = Label(main_screen, text='punchline', font=('Comfortaa'), bg='pink', width=20).grid(row=1, column=0, columnspan=2, pady=25)
display_joke = Button(main_screen, text='Alexa tell me a joke', font=('Comfortaa'), width=20, command=make_joke).grid(row=2, column=0, padx=5, pady=20)
punchline_button = Button(main_screen, text='Show Punchline',   font=('Comfortaa'), width=20).grid(row=2, column=1, pady=5, padx=20)
next_button = Button(main_screen, text='Next Joke', font=('Comfortaa'), width=20).grid(row=3, column=0, padx=5, pady=10)
quit_button = Button(main_screen, text='Quit', font=('Comfortaa'), width=20).grid(row=3, column=1, padx=5, pady=10)


main_screen.place(x=110, y=100, width=600, height=400)


root.mainloop()