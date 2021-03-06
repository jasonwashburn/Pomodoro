import math
from tkinter import *
from tkinter import ttk

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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps < 8:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
    elif reps >= 8:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)


# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tomato Background Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.gif')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title Label
title = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

# Start Button
start_button = ttk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = ttk.Button(text="Reset")
reset_button.grid(column=2, row=2)

# Counter Label
counter_label = Label(text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
counter_label.grid(column=1, row=3)

window.mainloop()
