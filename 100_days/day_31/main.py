from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --------------------------- DATA READING ----------------------------- # 
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ------------------------- BUTTON FUNCTIONS --------------------------- # 
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)  
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill='black')  
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')

def remove_card():
    next_card()

    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Setup the canvas with card image and text
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Labels

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0, relief=FLAT, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=remove_card, highlightthickness=0, relief=FLAT, borderwidth=0)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()