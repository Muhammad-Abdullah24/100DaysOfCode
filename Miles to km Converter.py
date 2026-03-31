from tkinter import *

def convert():
    miles = input.get()
    if miles:  # make sure it's not empty
        km_value = round(float(miles) * 1.609, 2)
        result_label.config(text=f"{km_value}")

# Window setup
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(400, 200)
window.config(padx=20, pady=20)

# Input field
input = Entry(width=10)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
