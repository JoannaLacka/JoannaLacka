from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry('600x400')

def open_file():
    filename = filedialog.askopenfilename(


    )

open_btn = Button(root, text="Open file", command=open_file)
open_btn.pack()

root.mainloop()