from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image app")
image_number = 0
my_label = Label()

images = [
    ImageTk.PhotoImage(Image.open("1.jpg")),
    ImageTk.PhotoImage(Image.open("2.jpg")),
    ImageTk.PhotoImage(Image.open("3.jpg"))]

def change_image(dir):
    global image_number
    if(image_number < len(images)-1 and dir == 1):
        image_number += 1
    elif(image_number > 0 and dir == -1):
        image_number -= 1
    else:
        return
    load_image(image_number)

def load_image(img_num):
    global my_label
    my_label.config(image=images[img_num])
    my_label.grid(row=0, column=0, columnspan=6)

load_image(0)

btn_prev = Button(root, text="Prev", command=lambda:change_image(-1))
btn_prev.grid(row=1, column=2)
btn_next = Button(root, text="Next", command=lambda:change_image(1))
btn_next.grid(row=1, column=3)

root.mainloop()