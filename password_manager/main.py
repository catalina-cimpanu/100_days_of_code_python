from tkinter import *
from tkinter import messagebox
import json
import random


# ---------------------------- Constants -------------------------------- #
BG = "#FEF6FB"
FG_TITLE = "#C84361"
FG = "#6C5070"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    global letters, numbers, symbols
    pass_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]
    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_password = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing data", message="You have an empty field")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details that you entered: \nWebsite: {website} \nUsername: {username} \nPassword: {password}\n\nIs this ok?")
        if is_ok:
            # f = open("passwords.txt", "a")
            # f.write(f"{website_data}|{username_data}|{password_data}\n")
            # f.close()
            try:
                with open("passwords.json", "r") as passwords_file:
                    # read old data
                    data = json.load(passwords_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as passwords_file:
                    json.dump(new_password, passwords_file, indent=4)
            else:
                # update json data
                data.update(new_password)
                # write json data to file
                with open("passwords.json", "w") as passwords_file:
                    json.dump(data, passwords_file, indent=4)
            finally:
                website_entry.delete(0, END)
                website_entry.focus()
                password_entry.delete(0, END)

# -------------------------- SEARCH PASSWORD --------------------------#
def find_password():
    searched_website = website_entry.get()
    try:
        with open("passwords.json", "r") as passwords_file:
            data = json.load(passwords_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found")
    else:
        if searched_website in data:
            username = data[searched_website]["username"]
            password = data[searched_website]["password"]
            messagebox.showinfo(title=searched_website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Info", message=f"There is no data for {searched_website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg=BG)

# Logo
canvas = Canvas(width=220, height=210, bg=BG, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 105, image=logo)
canvas.grid(column=1, row=0, sticky="ew")

# Labels
website_label = Label(text="Website", bg=BG, fg=FG)
website_label.grid(column=0, row=1, sticky="ew")

email_label = Label(text="Email/Username", bg=BG, fg=FG)
email_label.grid(column=0, row=2, sticky="ew")

password_label = Label(text="Password", bg=BG, fg=FG)
password_label.grid(column=0, row=3, sticky="ew")

# Entries and buttons
generate_pass_button = Button(text="Generate password", command=generate_password, bg=BG, fg=FG)
generate_pass_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", command=add_password, bg=BG, fg=FG)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

search_button = Button(text="Search", command=find_password, bg=BG, fg=FG)
search_button.grid(column=2, row=1, sticky="ew")

website_entry = Entry(bg=BG)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

username_entry = Entry(bg=BG)
username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
username_entry.insert(0, "name@email.com")

password_entry = Entry(bg=BG)
password_entry.grid(column=1, row=3, sticky="ew")

mainloop()
