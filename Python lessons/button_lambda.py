# metoda do której potrzeba dodać argumenty lambda

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x300")

def display_prompt(msg):
    messagebox.showinfo(title="Event", message=msg)

my_btn = Button(root,
    text="Get info",
    padx = 20,
    pady = 10,
    command=lambda:display_prompt("Działa"))

my_btn.pack()

root.mainloop()