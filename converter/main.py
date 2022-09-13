from tkinter import *


def button_clicked():
    try:
        miles = int(entry.get())
        result = round(miles * 1.60934, 2)
    except:
        result = "Please give a valid number"
    label_result = Label(text=f"{result}", font=("Arial", 16, "bold"), justify="center", padx=20, pady=20)
    label_result.grid(column=1, row=1)


window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
label_miles = Label(text="Miles", font=("Arial", 16, "bold"), justify="left", padx=20, pady=20)
label_miles.grid(column=2, row=0)

label_km = Label(text="Km", font=("Arial", 16, "bold"), justify="left", padx=20, pady=20)
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to", font=("Arial", 16, "bold"), justify="right", padx=20, pady=20)
label_equal.grid(column=0, row=1)

# Button
button = Button(text="Calculate", command=button_clicked, padx=10, pady=3)
button.grid(column=1, row=2)

# Entry
entry = Entry()
entry.grid(column=1, row=0)

window.mainloop()
