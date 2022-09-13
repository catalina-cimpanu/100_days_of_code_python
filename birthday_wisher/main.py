##################### Extra Hard Starting Project ######################
import random
from tkinter import *
import pandas
import datetime as dt
import smtplib

# constants
BACKGROUND = "#F8ECD1"
LIGHT = "#DEB6AB"
MEDIUM = "#AC7D88"
DARK = "#85586F"
FONT = ("Tahoma", 16, "bold")
MY_EMAIL = "username@email.com"
PASSWORD = "password"

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")


def update_data():
    name = person_entry.get()
    email = email_entry.get()
    try:
        day = int(bday_day_entry.get())
        month = int(bday_month_entry.get())
        year = int(bday_year_entry.get())
    except ValueError:
        greeting.config(text="Please only give numbers for the birthday")
    else:
        birthdays.loc[len(birthdays.index)] = [name, email, year, month, day]
        birthdays.to_csv("birthdays.csv", index=False)
    finally:
        person_entry.delete(0, END)
        email_entry.delete(0, END)
        bday_day_entry.delete(0, END)
        bday_month_entry.delete(0, END)
        bday_year_entry.delete(0, END)


# --------------------- Interface ----------------------------- #
window = Tk()
window.title("Birthday manager")
window.config(padx=30, pady=30, bg=BACKGROUND)

# Greeting
greeting = Label(text="Please give the name and bday: ", bg=BACKGROUND, fg=DARK, font=FONT)
greeting.grid(column=0, row=0, columnspan=7, sticky="ew", pady=5)

# Person data
person_label = Label(text="Person name: ", bg=BACKGROUND)
person_label.grid(column=0, row=1, padx=1, pady=3)
person_entry = Entry()
person_entry.grid(column=1, row=1, columnspan=6, sticky="ew", padx=1, pady=3)

email_label = Label(text="Email: ", bg=BACKGROUND)
email_label.grid(column=0, row=2, padx=1, pady=3)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=6, sticky="ew", padx=1, pady=3)

# B day data
bday_label = Label(text="Birthday: ", bg=BACKGROUND)
bday_label.grid(column=0, row=3, padx=1, pady=3)

bday_day_label = Label(text="Day: ", bg=BACKGROUND)
bday_day_label.grid(column=1, row=3, padx=1, pady=3)
bday_day_entry = Entry(width=10)
bday_day_entry.grid(column=2, row=3, padx=1, pady=3)

bday_month_label = Label(text="Month: ", bg=BACKGROUND)
bday_month_label.grid(column=3, row=3, padx=1, pady=3)
bday_month_entry = Entry(width=10)
bday_month_entry.grid(column=4, row=3, padx=1, pady=3)

bday_year_label = Label(text="Year: ", bg=BACKGROUND)
bday_year_label.grid(column=5, row=3, padx=1, pady=3)
bday_year_entry = Entry(width=10)
bday_year_entry.grid(column=6, row=3, padx=1, pady=3)

save = Button(text="Save", command=update_data, bg=LIGHT, padx=5, pady=2)
save.grid(column=3, row=4, pady=(20, 0))

window.mainloop()

# 2. Check if today matches a birthday in the birthdays.csv
# Get today
now = dt.datetime.now()
month = now.month
day = now.day

# Check if today is someone's bday
months = birthdays.loc[birthdays['month'] == month]
days = None
if not months.empty:
    days = months.loc[months["day"] == day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
bday_letter = None
bday_person_name = None
bday_person_email = None
todays_bdays = []
if not days.empty:
    for row in range(0, len(days)):
        bday_person_name = days.iloc[row]["name"]
        bday_person_email = days.iloc[row]["email"]
        todays_bdays.append(bday_person_name)
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter = letter.read()
            letter = letter.replace("[NAME]", f"{bday_person_name}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{bday_person_email}",
                                msg=f"Subject:Happy birthday\n\n{letter}")
