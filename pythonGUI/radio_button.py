import tkinter
from tkinter import IntVar, StringVar

root = tkinter.Tk()
root.title('Radio Button Basics')
root.iconbitmap('icon.ico')
root.geometry('400x400')
root.resizable(0, 0)


def make_label():
    if Number.get() == 1:
        num_label = tkinter.Label(output_frame, text='1 one 1')
        num_label.pack()
    elif Number.get() == 2:
        num_label = tkinter.Label(output_frame, text='2 two 2')
        num_label.pack()


input_frame = tkinter.LabelFrame(root, text='This is fun!!', width=350, height=100)
output_frame = tkinter.Frame(root, width=350, height=300)
input_frame.pack(padx=10, pady=5)
output_frame.pack(padx=15, pady=(0, 10))


Number = IntVar()
Number.set(2)
radio1 = tkinter.Radiobutton(input_frame, text='Print the number one', variable=Number, value=1)
radio2 = tkinter.Radiobutton(input_frame, text='Print the number two', variable=Number, value=2)
print_button = tkinter.Button(input_frame, text='Print the number!', command=make_label)


radio1.grid(row=0, column=0, padx=10, pady=10)
radio2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()