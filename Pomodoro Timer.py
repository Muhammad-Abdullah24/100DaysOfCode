import math
from tkinter import *
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
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer", fg=GREEN)
    checks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)

heading = Label(text= "Timer", font= (FONT_NAME, 40, "bold"), fg= GREEN, bg=YELLOW)
heading.grid(column= 1, row= 0)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
bg = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= bg)
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row= 1)

checkmark = "✔"
checks = Label(text= checkmark, font= (FONT_NAME, 15, "bold"), fg= GREEN, bg= YELLOW)
checks.grid(column= 1, row= 3)

start = Button(text="start", bg= RED, fg= "white", command= start_timer)
start.grid(column= 0, row= 2)

reset = Button(text= "reset", bg= RED, fg= "white", command= reset_timer)
reset.grid(column= 3, row= 2)


window.mainloop()