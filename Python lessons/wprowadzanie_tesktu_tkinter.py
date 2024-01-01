from tkinter import *
root = Tk()
root.geometry('600x300')

entry_w = Entry(root, width=50)
entry_w.pack()

def get_input(event):
    my_label = Label(root, text=entry_w.get())
    my_label.pack()

# my_btn = Button(root, text="Click me", command=get_input)
# my_btn.pack()
    
entry_w.bind('<Return>', get_input)

root.mainloop()