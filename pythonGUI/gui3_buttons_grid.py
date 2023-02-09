import tkinter

root = tkinter.Tk()
root.title('Buttons and grid')
root.iconbitmap('icon.ico')
root.geometry('500x500')
root.config(bg='yellow')
root.resizable(0,0)

name = tkinter.Button(root, bg='black', text='Hello everyone', foreground='yellow')
name.grid(row=0, column=0, padx=5)

time = tkinter.Button(root, bg='purple', text='time')
time.grid(row=0, column=2, padx=5)

place = tkinter.Button(root, bg='pink', text='Place', activebackground='green', activeforeground='red')
place.grid(row=0, column=3, padx=10, pady=10)

day = tkinter.Button(root, bg='red', text='Day', activebackground='green')
day.grid(row=1, column=0, padx=10, columnspan=3, sticky='we')

test1 = tkinter.Button(root, text='text1')
test2 = tkinter.Button(root, text='text2')
test3 = tkinter.Button(root, text='text3')
test4 = tkinter.Button(root, text='text4')
test5 = tkinter.Button(root, text='text5')
test6 = tkinter.Button(root, text='text6')

test1.grid(row=3, column=0, padx=5, pady=5, sticky='w')
test2.grid(row=3, column=1, padx=5, pady=5, sticky='w')
test3.grid(row=3, column=2, padx=5, pady=5, sticky='w')
test4.grid(row=4, column=0, padx=5, pady=5, sticky='w')
test5.grid(row=4, column=1, padx=5, pady=5, sticky='w')
test6.grid(row=4, column=2, padx=5, pady=5, sticky='w')



root.mainloop()