import tkinter
from tkinter import BOTH
from tkinter import END

root = tkinter.Tk()
root.title('Entry Basics')
root.iconbitmap('icon.ico')
root.geometry('450x400')
root.resizable(0, 0)


def make_label():
    # print('Hello tareq')
    text = tkinter.Label(output_frame, text=text_entry.get(), bg='#ff0000')
    text.pack()

    text_entry.delete(0, END)

def count_up(v):
    global value
    text = tkinter.Label(output_frame, text=v, bg='#ff0000')
    text.pack()

    value = v + 1


input_frame = tkinter.Frame(root, bg='#0000ff', width=500, height=100)
output_frame = tkinter.Frame(root, bg='#ff0000', width=500, height=250)
input_frame.pack(padx=10, pady=(10, 0))
output_frame.pack(padx=10, pady=(0, 10))

text_entry = tkinter.Entry(input_frame, width=50)
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(0)

print_button = tkinter.Button(input_frame, text='Print', command=make_label)
print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=20)

output_frame.pack_propagate(0)

value = 0
count_button = tkinter.Button(input_frame, text='Count!!!', command=lambda :count_up(value))
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

root.mainloop()