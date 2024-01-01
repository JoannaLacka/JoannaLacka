from tkinter import *
root = Tk()
root.geometry('600x400')
my_label = Label(root, text="Hejka, to jest etykieta")
my_label.config(
    background = "#555",
    fg = "#ccc",
    font = ("Arial", 20),
    padx = 20,
    pady = 10
)
my_label.pack()

root.mainloop()