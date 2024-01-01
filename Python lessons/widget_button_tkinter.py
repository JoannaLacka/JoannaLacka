from tkinter import *
import datetime
root = Tk()
root.geometry('600x400')

def get_date():
    data = datetime.datetime.now()
    data_label = Label(root, text=data, fg="#ff0000")
    data_label.pack()

btn = Button(root, 
    text="Get date",
    background="#555",
    fg="#aaa",
    padx = 20,
    pady = 10,
    command=get_date)

btn.pack()

root.mainloop()