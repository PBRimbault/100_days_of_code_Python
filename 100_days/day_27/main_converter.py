from tkinter import *

# Button
def calculate():
    miles = float(input1.get())
    kilometers = miles * 1.609
    output1.config(text=kilometers)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_label = Label(text="Miles", font=("Arial", 14))
mile_label.grid(column=2, row=0)

Km_label = Label(text="Km", font=("Arial", 14))
Km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to ", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)

input1 = Entry(width=7)
input1.grid(column=1, row=0)

output1 = Label(text="0", font=("Arial", 14))
output1.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()