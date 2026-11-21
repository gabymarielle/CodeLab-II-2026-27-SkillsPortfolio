from tkinter import *


with open("studentMarks.txt", "r", encoding='utf-8') as file:
    records = file.readlines()
    file.close()

def all_records():
    all_data = ""
    avg_percentage = 0

    for i in range(1, len(records)):
        data = records[i].strip().split(",")
        coursework = int(data[2]) + int(data[3]) + int(data[4])
        exam = int(data[5])
        percentage = (coursework + exam) / 160 * 100
        avg_percentage = avg_percentage + percentage

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"
        
        all_data = all_data + "Student Number: " + data[0] + "\n"
        all_data = all_data + "Student Name: " + data[1] + "\n"
        all_data = all_data + "Total Coursework Mark: " + str(coursework) + "\n"
        all_data = all_data + "Exam: " + str(exam) + "\n"
        all_data = all_data + "Overall Percentage: " + str(round(percentage, 1)) + "%\n"
        all_data = all_data + "Student Grade: " + grade + "\n"
        all_data = all_data + "\n"

    student_num = len(records) - 1
    average = avg_percentage / student_num

    all_data = all_data + "TOTAL NUMBER OF STUDENTS: " + str(student_num) + "\n"
    all_data = all_data + "AVERAGE PERCENTAGE OF THIS CLASS: " + str(round(average, 1)) + "%\n"

    main_output.config(state=NORMAL)
    main_output.delete("1.0", END)
    main_output.insert(END, all_data)
    main_output.config(state=DISABLED)



root = Tk()
root.title('Random Jokes')
root.config(bg='white')
root.geometry('750x600')
root.resizable(0,0)


menu_frame = Frame(root, bg='#39719E')
view_all = Button(menu_frame, text='View All', width=15, command=all_records)
view_all.pack(pady=(80, 15))
view_indv = Button(menu_frame, text='View Individual', width=15).pack(pady=15)
view_high = Button(menu_frame, text='View Highest', width=15).pack(pady=15)
view_low = Button(menu_frame, text='View Lowest', width=15).pack(pady=15)
sort_rec = Button(menu_frame, text='Sort', width=15).pack(pady=15)
add_rec = Button(menu_frame, text='Add', width=15).pack(pady=15)
del_rec = Button(menu_frame, text='Delete', width=15).pack(pady=15)
upd_rec = Button(menu_frame, text='Update', width=15).pack(pady=15)

menu_frame.pack(side=LEFT)
menu_frame.place(width=180, height=600)



main_frame = Frame(root, bg='#F0F0F0')
main_output = Text(main_frame)
main_output.pack(side=LEFT, fill=BOTH, expand=True)



main_frame.place(x=200, y=20, width=530, height=560)






root.mainloop()