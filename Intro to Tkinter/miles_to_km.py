import math
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(height=200,width=300)
window.config(padx=75,pady=50)




#Creating Text Input

miles_input = Entry()
miles_input.grid(column=1,row=0)

#Creating Label Statements

miles = Label(text="Miles")
miles.grid(column=2,row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

km_answer = Label()
km_answer.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

#Button function

# multiplying the number of miles by 1.6

def calc_miles_to_kilometer():
    result = round((int(miles_input.get()) * 1.6),2)
    km_answer["text"] = str(result)

#Creating Button

button = Button(text="Calculate",command=calc_miles_to_kilometer)
button.grid(column=1,row=2)


window.mainloop()