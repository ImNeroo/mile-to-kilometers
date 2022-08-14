import tkinter


def button_clicked():
    miles = input_number.get()
    km = round(float(miles) * 1.609, 2)
    new_number_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km converter")
# window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

input_number = tkinter.Entry(width=7)
input_number.grid(column=1, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

new_number_label = tkinter.Label(text="0")
new_number_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
