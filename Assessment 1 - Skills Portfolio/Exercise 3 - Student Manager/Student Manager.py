from tkinter import *


with open("studentMarks.txt", "r", encoding='utf-8') as file:
    records = file.readlines()
    file.close()

def get_grade(percentage):
    global grade
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def show_text(text):
    view_all_output.config(state=NORMAL)
    view_all_output.delete("1.0", END)
    view_all_output.insert(END, text)
    view_all_output.config(state=DISABLED)
        
def all_records():
    search_frame.place_forget()
    all_data = ""
    avg_percentage = 0

    for i in range(1, len(records)):
        data = records[i].strip().split(",")
        coursework = int(data[2]) + int(data[3]) + int(data[4])
        exam = int(data[5])
        percentage = (coursework + exam) / 160 * 100
        avg_percentage = avg_percentage + percentage
        all_data = all_data + "Student Number: " + data[0] + "\n"
        all_data = all_data + "Student Name: " + data[1] + "\n"
        all_data = all_data + "Total Coursework Mark: " + str(coursework) + "\n"
        all_data = all_data + "Exam: " + str(exam) + "\n"
        all_data = all_data + "Overall Percentage: " + str(round(percentage, 1)) + "%\n"
        all_data = all_data + "Student Grade: " + get_grade(percentage) + "\n"
        all_data = all_data + "\n"

    student_num = len(records) - 1
    average = avg_percentage / student_num
    all_data = all_data + "TOTAL NUMBER OF STUDENTS: " + str(student_num) + "\n"
    all_data = all_data + "AVERAGE PERCENTAGE OF THIS CLASS: " + str(round(average, 1)) + "%\n"
    show_text(all_data)

def individual_records():
    search_frame.place(x=0, y=5)
    search_frame.lift()
    search_entry.delete(0, END)
    show_text("")

def search():
    enter_num = search_entry.get().strip()
    text = "Student not found.."
    for i in range(1, len(records)):
        data = records[i].strip().split(",")
        if data[0] == enter_num:
            coursework = int(data[2]) + int(data[3]) + int(data[4])
            exam = int(data[5])
            percentage = (coursework + exam) / 160 * 100
            text = "Student Number: " + data[0] + "\n"
            text = text + "Student Name: " + data[1] + "\n"
            text = text + "Total Coursework Mark: " + str(coursework) + "\n"
            text = text + "Exam: " + str(exam) + "\n"
            text = text + "Overall Percentage: " + str(round(percentage, 1)) + "%\n"
            text = text + "Student Grade: " + get_grade(percentage) + "\n"
    show_text(text)



root = Tk()
root.title('Random Jokes')
root.config(bg='white')
root.geometry('750x600')
root.resizable(0,0)


menu_frame = Frame(root, bg='#39719E')
view_all = Button(menu_frame, text='View All', width=15, command=all_records)
view_all.pack(pady=(80, 15))
view_indv = Button(menu_frame, text='View Individual', width=15, command=individual_records)
view_indv.pack(pady=15)
view_high = Button(menu_frame, text='View Highest', width=15).pack(pady=15)
view_low = Button(menu_frame, text='View Lowest', width=15).pack(pady=15)
sort_rec = Button(menu_frame, text='Sort', width=15).pack(pady=15)
add_rec = Button(menu_frame, text='Add', width=15).pack(pady=15)
del_rec = Button(menu_frame, text='Delete', width=15).pack(pady=15)
upd_rec = Button(menu_frame, text='Update', width=15).pack(pady=15)

menu_frame.pack(side=LEFT)
menu_frame.place(width=180, height=600)



main_frame = Frame(root, bg='#F0F0F0')

search_frame = Frame(main_frame, bg='#F0F0F0')
search_label = Label(search_frame, text="Enter student number:", bg='#F0F0F0')
search_label.pack(side=LEFT, padx=10)
search_entry = Entry(search_frame)
search_entry.pack(side=LEFT)
search_button = Button(search_frame, text="Search", command=search)
search_button.pack(side=LEFT, padx=5)

view_all_output = Text(main_frame, state=DISABLED)
view_all_output.place(x=0, y=40, width=530, height=520)



main_frame.place(x=200, y=20, width=530, height=560)






root.mainloop()