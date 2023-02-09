import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('Image basics!')
root.iconbitmap('icon.ico')
root.geometry('700x800+500+0')


def make_image():
    # use PIL for jpg
    global cat_image
    cat_image = ImageTk.PhotoImage(Image.open('cat (1).jpg'))
    cat_label = tkinter.Label(root, image=cat_image)
    cat_label.pack()


#Basics works for png file
my_image = tkinter.PhotoImage(file='blueberry (1).png')
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_image_two = tkinter.PhotoImage(file='rocket2 (1).png')
my_label_two = tkinter.Label(root, image=my_image_two)
my_label_two.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

# cat_image = tkinter.PhotoImage(file='cat (1).jpg')
# cat_label = tkinter.Label(root, image=cat_image)
# cat_label.pack()


make_image()
root.mainloop()