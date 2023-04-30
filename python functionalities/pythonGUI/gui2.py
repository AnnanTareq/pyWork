import tkinter
from tkinter import BOTH

root = tkinter.Tk()
root.config(bg='red')
root.title('Homepage')
root.geometry('300x300+300+300')
root.resizable(0, 0)

new_label = tkinter.Label(root, text='Hi! Welcome to America Bangladesh Foundation!')
new_label.pack()

new_label2 = tkinter.Label(root, text='This foundation works for people', font=('Times New Roman', 15, 'italic', 'bold'), bg='green')
new_label2.pack()

new_label3 = tkinter.Label(root)
new_label3.config(text='first Test')
new_label3.config(font=('Arial', 14))
new_label3.config(bg='yellow')
new_label3.pack(padx=20, pady=20)

new_label4 = tkinter.Label(root, text='4th Line', bg='brown', foreground='white', font=('calibri', 25))
new_label4.pack(pady=(0, 20), ipady=20, ipadx=20, anchor='w')

new_label5 = tkinter.Label(root, text='5th Line', bg='pink', fg='blue')
# new_label5.pack(fill='both', expand=True)  #we can use it without import any extra library
new_label5.pack(fill=BOTH, expand=True, padx=10, pady=10)


root.mainloop()
