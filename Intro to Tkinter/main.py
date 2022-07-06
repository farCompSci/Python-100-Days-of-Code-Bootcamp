# import tkinter
from tkinter import *
#meaning import every class

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Creating a Label

my_label = Label(text="I am a label",font=("Arial","24","bold"))
# my_label.pack()
my_label.grid(column=0,row=0)

#Modifying text

my_label.config(text="New Text")
# or my_label["text"] = "New Text"

#Creating a function that would occur when button is clicked

def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    my_label["text"] = input.get()

def new_button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    my_label["text"] = "Button got clicked"

#Creating a button

button = Button(text="Click",command=button_clicked)
# button.pack()
# button.place(x=230,y=150)
button.grid(column=1,row=1)
# button.config(padx=20,pady=20)

new_button = Button(text="Click",command=new_button_clicked)
new_button.grid(column=2,row=0)

#Working with input

input = Entry(width=10)
# input.pack()
input.grid(column=3,row=2)


window.mainloop()

# def add(*args):
#     return sum(args)
#
# total = add(1,4,5)
# print(total)

# def operations(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n
#
# print(operations(4,multiply=6,add=5))