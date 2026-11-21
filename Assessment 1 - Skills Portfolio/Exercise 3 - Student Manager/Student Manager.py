from tkinter import *





root = Tk()
root.title('Random Jokes')
root.config(bg='white')
root.geometry('750x600')
root.resizable(0,0)


menu_frame = Frame(root, bg='#39719E')
view_all = Button(menu_frame, text='View All', width=15).pack(pady=(80, 15))
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


main_frame.place(x=200, y=20, width=530, height=500)






root.mainloop()