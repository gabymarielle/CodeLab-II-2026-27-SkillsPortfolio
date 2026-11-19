from tkinter import *
import random


root = Tk()
root.title('Random Jokes')
root.config(bg='pink')
root.geometry('750x500')
root.resizable(0,0)

# Open the randomJokes.txt file
with open("randomJokes.txt", "r", encoding='utf-8') as file:
    data = file.readline()
    print(data)

# Main Screen
main_screen = Frame(root, bg="pink")
joke = Label(main_screen, text=f'{data}', font=('Comfortaa'), bg='pink').grid(row=0, column=0, columnspan=2, pady=20)
display_joke = Button(main_screen, text='Alexa tell me a joke', font=('Comfortaa'), width=20).grid(row=1, column=0, padx=5, pady=10)
punchline_button = Button(main_screen, text='Show Punchline', font=('Comfortaa'), width=20).grid(row=1, column=1, pady=5, padx=10)
next_button = Button(main_screen, text='Next Joke', font=('Comfortaa'), width=20).grid(row=2, column=0, padx=5, pady=10)
quit_button = Button(main_screen, text='Quit', font=('Comfortaa'), width=20).grid(row=2, column=1, padx=5, pady=10)


main_screen.place(x=100, y=100, width=800, height=400)


root.mainloop()