from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#4E944F"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    global reps, checkmarks
    reps = 0
    checkmarks = ""
    checkmark.config(text=checkmarks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # note: has to be increased here, otherwise it starts with long break cuz 0/8==0
    if reps % 8 == 0:   # time for break, 8 cycles
        print(reps)
        countdown(LONG_BREAK_MIN*60)
        title_label.config(text="Long Break", fg=RED)
    else:  # still working
        print(reps)
        if reps % 2 == 0:  # break
            countdown(SHORT_BREAK_MIN*60)
            title_label.config(text="Short Break", fg=PINK)
        else:  # work
            countdown(WORK_MIN*60)
            global checkmarks
            title_label.config(text="Work", fg=GREEN)
            checkmark.config(text=checkmarks)
            checkmarks += '✔'


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown (secs):
    canvas.itemconfig(timer_text, text=f"{secs//60}:{f'0{secs%60}' if secs%60<10 else secs%60}")
    if secs > 0:
        global timer
        timer = window.after(1000, countdown, secs-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=30, bg=YELLOW)

# Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font={FONT_NAME, 35, "bold"})
canvas.grid(column=1, row=1)

# Title
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, padx=10, pady=5, font={FONT_NAME, 50, "bold"})
title_label.grid(column=1, row=0)

# Checkmark
checkmark = Label(bg=YELLOW, fg=GREEN, padx=10, pady=5, font={FONT_NAME, 50, "bold"})
checkmark.grid(column=1, row=4)

# Buttons
start_button = Button(text="Start", command=start_timer, bg=YELLOW, fg=GREEN, activebackground=PINK, padx=5, pady=2, font={FONT_NAME, 16, "bold"})
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=timer_reset, highlightthickness=0, bg=YELLOW, fg=GREEN,  activebackground=PINK, padx=5, pady=2, font={FONT_NAME, 16, "bold"})
reset_button.grid(column=2, row=3)


window.mainloop()

