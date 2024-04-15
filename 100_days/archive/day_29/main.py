from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = entry_website.get()
    email_text = entry_email_uname.get()
    password_text = entry_password.get()

    if website_text == '' or password_text == '' or email_text == '':
        messagebox.showerror(title='Oops', message="Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text} \nPassword: {password_text} \nIs this OK to save?")

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")
                data_file.close()

            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, background='white')

canvas = Canvas(width=200, height=200, background='white', highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
label_website=Label(text="Website:", background='white')
label_website.grid(column=0, row=1)
 
label_password = Label(text="Password:", background='white')
label_password.grid(column=0, row=3)

label_email_uname = Label(text="Email/Username:", background='white')
label_email_uname.grid(column=0, row=2)

# Entry blocks
entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, 'patrick.rimbault@gmail.com')

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")
 
# Buttons
generate_btn = Button(text="Generate Password", background='white', command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, background='white', command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
 
canvas.mainloop()