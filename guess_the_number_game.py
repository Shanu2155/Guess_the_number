import random

from docutils.utils.math.math2html import Label
from tkinter import *

r = random.randint(1, 101)


# def value1():
#  c = no_of_chances.get()
chances = 0


def getval():
    global chances
    chances = int(no_of_chances.get())
    lab.config(text="No. of chances left are " + str(chances))
    r1.destroy()
    r2.destroy()
    r3.destroy()


def check(event):
    global chances
    c = chances
    num = int(entry.get())
    entry.delete(0, 'end')
    if num > r:
        msg = "HIGH"
    if num < r:
        msg = "LOW"
    if num == r:
        msg = "CORRECT.....You Won"
    label1.config(text="Number "+str(num)+" is "+msg)
    c -= 1
    chances = c
    lab.config(text="No. of chances left are " + str(chances))
    if c == 0:
        # button.destroy()
        label1.config(text="Number is " + str(r) + " and u lost the game")


root = Tk()

lab = Label(root)
lab.grid(row=0, columnspan=2)
no_of_chances = IntVar()
r1 = Radiobutton(root, text="Easy", variable=no_of_chances, value=15, command=getval)
r2 = Radiobutton(root, text="Medium", variable=no_of_chances, value=10, command=getval)
r3 = Radiobutton(root, text="Hard", variable=no_of_chances, value=5, command=getval)
r1.grid(row=0, column=0)
r2.grid(row=0, column=1)
r3.grid(row=0, column=2)
label = Label(root, text="Enter number to check").grid(row=1, column=0)
entry = Entry(root)
entry.grid(row=1, column=1)
# button = Button(root, text="Check")
entry.bind("<Return>", check)
# button.grid(columnspan=2)
label1 = Label(root)
label1.grid(row=3, columnspan=2)

root.mainloop()


