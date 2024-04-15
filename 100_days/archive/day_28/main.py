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
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    tick_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps    
    reps += 1
    tick_count = 0
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f'0{count_min}'

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# Setup the canvas with tomato image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 45, 'bold'), foreground=GREEN, background=YELLOW,)
timer_label.grid(column=1, row=0)

tick_label = Label(font=(FONT_NAME, 25), foreground=GREEN, background=YELLOW)
tick_label.grid(column=1, row=3)

#Buttons
start_button = Button(text="Start", font=(FONT_NAME, 15), bg='white', border='0', command=start_timer)
start_button.grid(column=0, row=2, sticky='e')

reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg='white', border='0', command=reset_timer)
reset_button.grid(column=2, row=2, sticky='w')

window.mainloop()