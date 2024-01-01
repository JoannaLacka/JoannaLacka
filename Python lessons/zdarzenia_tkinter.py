from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x300")

def my_func(event):
    messagebox.showinfo(title="Event", message="Działa")
def my_func2(event):
    messagebox.showinfo(title="Event", message="Funkcja 2")

root.bind('<Button-1>',my_func)
root.bind('<Button-1>',my_func2, add='+')
root.mainloop()