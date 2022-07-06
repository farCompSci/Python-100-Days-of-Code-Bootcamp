from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="Timer")
    title_text.config(text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_minutes = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)
        title_text.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        title_text.config(text="Break",fg=PINK)
    else:
        count_down(work_minutes)
        title_text.config(text="Work",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count%60
    # if count_sec == 0:
    #     count_sec = "00" # Dynamic Typing to change the type of the variable count_sec when == 0
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-120)
    else:
        start_timer()
        marks = ""
        for _ in range(0,math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

title_text = Label(text="Timer",font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
title_text.grid(column=1,row=0)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_label = Label(bg=YELLOW,fg=GREEN)
check_label.grid(column=1,row=3)

# count_down(5)





window.mainloop()