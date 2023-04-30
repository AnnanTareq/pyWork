import tkinter
from tkinter import BOTH

root = tkinter.Tk()
root.title('New page')
root.geometry('400x400')


pack_frame1 = tkinter.Frame(root, bg='red')
grid_frame1 = tkinter.Frame(root, bg='blue')
grid_frame2 = tkinter.LabelFrame(root, text='GridSystemRules', borderwidth=15)


pack_frame1.pack(fill=BOTH, expand=True)
grid_frame1.pack(fill='y', expand=True)
grid_frame2.pack(fill=BOTH, expand=True)

tkinter.Label(pack_frame1, text='text11').pack()
tkinter.Label(pack_frame1, text='text12').pack()
tkinter.Label(pack_frame1, text='text13').pack()

tkinter.Label(grid_frame1, text='text11').grid(row=0, column=0)
tkinter.Label(grid_frame1, text='text12').grid(row=0, column=1)
tkinter.Label(grid_frame1, text='text13').grid(row=0, column=2)

tkinter.Label(grid_frame2, text='text21').grid(row=0, column=1)
tkinter.Label(grid_frame2, text='text22').grid(row=1, column=1)

root.mainloop()