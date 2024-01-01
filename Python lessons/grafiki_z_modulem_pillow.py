# instalacja modułu pillow pip install pillow

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('600x300')
img = ImageTk.PhotoImage(Image.open("1.jpg"))
my_label = Label(image=img)
my_label.pack()

root.mainloop()