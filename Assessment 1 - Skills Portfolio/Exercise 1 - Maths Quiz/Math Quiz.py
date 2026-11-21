from tkinter import *
import random 
import operator

num1 = 0
num2 = 0
totalQues = 10
currentDifficulty = 'easy'

def displayMenu(main_frame):
    main_frame.tkraise()

def startQuiz(difficulty):
    global numQues, score, currentDifficulty
    currentDifficulty = difficulty
    numQues = 0
    score = 0
    quiz_title.config(text=f'{difficulty.capitalize()} Difficulty')
    show_score.config(text='Score: 0')
    nextQuestion()


# redefine with actual values
def easy_diff():
    startQuiz('easy')
def moderate_diff():
    startQuiz('moderate')
def advanced_diff():
    startQuiz('advanced')


#required function
def decideOperation():
    operation = ['+', '-']
    symbol = random.choice(operation)
    return symbol

#required function
def displayProblem(num1, num2):
    oper = decideOperation()
    question = f"{num1} {oper} {num2}"
    return question

#required function
def randomInt(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        return num1, num2
    elif difficulty == 'moderate':
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        return num1, num2
    elif difficulty == 'advanced':
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        return num1, num2

def askQuestion(difficulty):
    global current_answer, attempts
    attempts = 2
    num1, num2 = randomInt(difficulty)
    question = displayProblem(num1, num2)

    current_answer = eval(question)

    return question

def isCorrect():
    global attempts, score
    user_input = answer_input.get().strip()
    answer_input.delete(0, END)

    try:
        user_num = int(user_input)
    except ValueError:
        feedback.config(text='Please enter a valid number.')
        return                        # invalid input doesn't use an attempt

    if user_num == current_answer:
        feedback.config(text="Correct!")
        if attempts == 2:
            score += 10
        else:
            score += 5
        show_score.config(text=f'Score: {score}')
        #if else for attempt -> if attempt = 2 -> score += 10 | else -> score += 5 
        root.after(1000, nextQuestion)   # next question
    else:
        attempts -= 1
        if attempts == 0:
            feedback.config(text=f'Out of attempts! Answer: {current_answer}')
            root.after(1500, nextQuestion)   # next question
        else:
            feedback.config(text=f'Incorrect. {attempts} attempt(s) left.')
 
def nextQuestion():
    global numQues
    if numQues == totalQues:
        result_score.config(text=f'Your Score: {score}')
        grades.config(text=displayResults())
        displayMenu(result_frame)
        return
    numQues += 1
    feedback.config(text='')
    quiz_question.config(text=askQuestion(currentDifficulty))
    displayMenu(quiz_frame)
    
def displayResults():
    global score
    if score >= 90:
        return 'A+! HUSS HUSS HUSS'
    elif score >= 80:
        return 'A! Galing mo boi!'
    elif score >= 70:
        return 'You got a B!'
    elif score >= 60:
        return 'You got a C!'
    elif score >= 50:
        return 'You got a D!'
    elif score >= 40:
        return 'You got an F.'
    else:
        return 'Grade is unranked. Do better son.'


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


# Quiz Frame
quiz_frame = Frame(root, bg='pink')
quiz_title = Label(quiz_frame, text="", font=('Comfortaa'), bg='pink')
quiz_title.pack()
quiz_question = Label(quiz_frame, text="", font=('Comfortaa'))  
quiz_question.pack()
answer_input = Entry(quiz_frame)
answer_input.pack(pady=10)
feedback = Label(quiz_frame, text="", bg='pink')
feedback.pack()
show_score = Label(quiz_frame, text="Score: ", font=('Comfortaa'))
show_score.pack()
quiz_button = Button(quiz_frame, text="Submit", font=('Comfortaa'), command=isCorrect)
quiz_button.pack(pady=10)

quiz_frame.place(x=100, y=100, width=400, height=400)


# Results Frame
result_frame = Frame(root, bg='pink')
result_score = Label(result_frame, text="", font=('Comfortaa'), bg='pink')
result_score.pack()
grades = Label(result_frame, text="", font=('Comfortaa'))
grades.pack()
back_button = Button(result_frame, text="Return", font=('Comfortaa'), command=lambda: displayMenu(main_frame)).pack()


result_frame.place(x=100, y=100, width=400, height=400)

displayMenu(main_frame)
root.mainloop()