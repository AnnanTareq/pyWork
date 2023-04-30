import tkinter
import os

root = tkinter.Tk()
root.title('America Bangladesh Foundation')
root.iconbitmap('D:/udemy-oopPython/pythonGUI/Custom-Icon-Design-All-Country-Flag-Bangladesh-Flag.ico')
root.geometry('400x500')
root.resizable(0, 0)
root.config(bg='blue')


top = tkinter.Toplevel()
top.title('About US')
top.geometry('200x200+300+300')
top.resizable(0, 0)
top.config(bg='grey')


root.mainloop()
