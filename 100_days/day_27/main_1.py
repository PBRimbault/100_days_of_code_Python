from tkinter import *

# Button
def button_clicked():
    print("I got clicked")
    new_text = input1.get()    
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label
my_label = Label(text="Clicker Count", font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input1 = Entry(width=10)
print(input1.get())
input1.grid(column=3, row=2)

window.mainloop()