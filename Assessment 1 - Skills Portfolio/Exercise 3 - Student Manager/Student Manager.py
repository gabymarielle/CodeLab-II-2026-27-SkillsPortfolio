from tkinter import *
import json

# Opens the json file
with open("studentMarks.json", "r") as file:
    records = json.load(file)
    file.close()

# Function where new data gets added or removed in the json file
def save():
    with open("studentMarks.json", "w") as file:
        json.dump(records, file, indent=4)

# Gets the data in the file and calculates it all together to get the percentage of the combined scores of the students
def get_percentage(data):
    marks = sum(data["classwork"]) + data["exam"]
    return marks / 160 * 100

# If statement to decide what grade a student gets depending on their percentage
def get_grade(percentage):
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

# A function to easily print out student data and easier to put in every function 
def student_text(data):
    coursework = sum(data["classwork"])
    percentage = get_percentage(data)
    text = "Student Number: " + str(data["id"]) + "\n"
    text = text + "Student Name: " + data["student"] + "\n"
    text = text + "Total Coursework Mark: " + str(coursework) + "\n"
    text = text + "Exam: " + str(data["exam"]) + "\n"
    text = text + "Overall Percentage: " + str(round(percentage, 1)) + "%\n"
    text = text + "Student Grade: " + get_grade(percentage) + "\n"
    return text

def hide():
    search_frame.place_forget()
    sort_frame.place_forget()
    form_frame.place_forget()

def all_records():
    hide()
    all_data = ""
    avg_percentage = 0

    for data in records:
        all_data = all_data + student_text(data) + "\n"
        avg_percentage = avg_percentage + get_percentage(data)

    all_data = all_data + "TOTAL NUMBER OF STUDENTS: " + str(len(records)) + "\n"
    all_data = all_data + "AVERAGE PERCENTAGE OF THIS CLASS: " + str(round(avg_percentage / len(records), 1)) + "%\n"
    show_text(all_data)

def individual_records():
    hide()
    search_frame.place(x=0, y=5)
    search_frame.lift()
    search_entry.delete(0, END)
    show_text("")

def search():
    enter_num = search_entry.get().strip()
    text = "Student not found.."
    for data in records:
        if str(data["id"]) == enter_num:
            text = student_text(data)
    show_text(text)

def view_highest():
    hide()
    highest = records[0]
    for data in records:
        if get_percentage(data) > get_percentage(highest):
            highest = data
    show_text("STUDENT WITH HIGHEST MARK:\n\n" + student_text(highest)) 

def view_lowest():
    hide()
    lowest = records[0]
    for data in records:
        if get_percentage(data) < get_percentage(lowest):
            lowest = data
    show_text("STUDENT WITH LOWEST MARK:\n\n" + student_text(lowest)) 

def sort():
    hide()
    sort_frame.place(x=0, y=5)
    show_text("")

def sort_ascending():
    students = records.copy()
    students.sort(key=get_percentage)
    text = "SORTED STUDENTS FROM LOWEST TO HIGHEST:\n\n"
    for data in students:
        text = text + student_text(data) + "\n"
    show_text(text)

def sort_descending():
    students = records.copy()
    students.sort(key=get_percentage, reverse=True)
    text = "SORTED STUDENTS FROM HIGHEST TO LOWEST:\n\n"
    for data in students:
        text = text + student_text(data) + "\n"
    show_text(text)

def find(id):
    for data in records:
        if str(data["id"]) == id:
            return data

def show_form(count, text, command):
    hide()
    show_text("")
    form_frame.place(x=0, y=0)

    for i in range(4):
        entries[i].delete(0, END)
        if i < count:
            labels[i].place(x=20, y=20 + i * 50)
            entries[i].place(x=250, y=20 + i * 50)
        else:
            labels[i].place_forget()
            entries[i].place_forget()

    form_btn.config(text=text, command=command)
    form_btn.place(x=20, y=240)
    msg.config(text="")
    msg.place(x=20, y=280)

def add_student():
    if find(entries[0].get()) != None:
        msg.config(text="ID already exists", fg="red")
        return
    if len(entries[0].get()) != 4 or not entries[0].get().isdigit():
        msg.config(text="ID must be exactly 4 numbers", fg="red")
        return

    try:
        new_id = int(entries[0].get())
        name = entries[1].get()
        classwork = []
        for mark in entries[2].get().split(","):
            if int(mark) < 0 or int(mark) > 20:
                msg.config(text="Each coursework mark must be 0 to 20", fg="red")
                return
            classwork.append(int(mark))
        exam = int(entries[3].get())
        if exam < 0 or exam > 100:
            msg.config(text="Exam must be 0 to 100", fg="red")
            return
    except ValueError:
        msg.config(text="Invalid input", fg="red")
        return

    records.append({"id": new_id, "student": name, "classwork": classwork, "exam": exam})
    save()
    msg.config(text="Student added!", fg="green")

def delete_student():
    student = find(entries[0].get())
    if student == None:
        msg.config(text="Student not found", fg="red")
        return

    records.remove(student)
    save()
    msg.config(text="Student deleted!", fg="green")


def update_student():
    student = find(entries[0].get())
    if student == None:
        msg.config(text="Student not found", fg="red")
        return

    try:
        classwork = student["classwork"]
        exam = student["exam"]
        if entries[2].get() != "":
            classwork = []
            for mark in entries[2].get().split(","):
                if int(mark) < 0 or int(mark) > 20:
                    msg.config(text="Each coursework mark must be 0 to 20", fg="red")
                    return
                classwork.append(int(mark))
        if entries[3].get() != "":
            exam = int(entries[3].get())
            if exam < 0 or exam > 100:
                msg.config(text="Exam must be 0 to 100", fg="red")
                return
    except ValueError:
        msg.config(text="Invalid input", fg="red")
        return

    if entries[1].get() != "":
        student["student"] = entries[1].get()
    student["classwork"] = classwork
    student["exam"] = exam
    save()
    msg.config(text="Student updated!", fg="green")
    


root = Tk()
root.title('Random Jokes')
root.config(bg='white')
root.geometry('750x600')
root.resizable(0,0)

# Side frame to display buttons for the user
menu_frame = Frame(root, bg='#39719E')
view_all = Button(menu_frame, text='View All', width=15, command=all_records)
view_all.pack(pady=(80, 15))
view_indv = Button(menu_frame, text='View Individual', width=15, command=individual_records)
view_indv.pack(pady=15)
view_high = Button(menu_frame, text='View Highest', width=15, command=view_highest)
view_high.pack(pady=15)
view_low = Button(menu_frame, text='View Lowest', width=15, command=view_lowest)
view_low.pack(pady=15)
sort_rec = Button(menu_frame, text='Sort', width=15, command=sort)
sort_rec.pack(pady=15)
add_rec = Button(menu_frame, text='Add', width=15, command=lambda: show_form(4, "Add", add_student))
add_rec.pack(pady=15)
del_rec = Button(menu_frame, text='Delete', width=15, command=lambda: show_form(1, "Delete", delete_student))
del_rec.pack(pady=15)
upd_rec = Button(menu_frame, text='Update', width=15, command=lambda: show_form(4, "Update", update_student))
upd_rec.pack(pady=15)

menu_frame.pack(side=LEFT)
menu_frame.place(width=180, height=600)


# Main frame where all output comes out 
main_frame = Frame(root, bg='#F0F0F0')

view_all_output = Text(main_frame, state=DISABLED, cursor="arrow")
form_frame = Frame(view_all_output, bg='white', width=500, height=320)
labels = []
entries = []
for text in ["Student ID:", "Name:", "Classwork (e.g. 20,30,25):", "Exam mark:"]:
    labels.append(Label(form_frame, text=text, bg='white'))
    entries.append(Entry(form_frame, bg='#E8E8E8', width=30))
form_btn = Button(form_frame, width=15)
msg = Label(form_frame, bg='white')
view_all_output.place(x=0, y=40, width=530, height=520)

search_frame = Frame(main_frame, bg='#F0F0F0')
search_label = Label(search_frame, text="Enter student number:", bg='#F0F0F0')
search_label.pack(side=LEFT, padx=10)
search_entry = Entry(search_frame)
search_entry.pack(side=LEFT)
search_button = Button(search_frame, text="Search", command=search)
search_button.pack(side=LEFT, padx=10)

sort_frame = Frame(main_frame, bg='#F0F0F0')
asc = Button(sort_frame, text='Ascending', command=sort_ascending)
asc.pack(side=LEFT, padx=5)
desc = Button(sort_frame, text='Descending', command=sort_descending)
desc.pack(side=LEFT)



main_frame.place(x=200, y=20, width=530, height=800)






root.mainloop()