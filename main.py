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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tomato Background Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.gif')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title Label
title = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 18, "normal"))
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 18, "normal"))
reset_button.grid(column=2, row=2)

# Counter Label
counter_label = Label(text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
counter_label.grid(column=1, row=3)


window.mainloop()
