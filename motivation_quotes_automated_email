import smtplib
import datetime as dt
import random

# get today -------------------------------
now = dt.datetime.now()
day = now.weekday()

# get quotes -------------------------------
with open("quotes.txt") as file:
    quotes = file.readlines()
quote_of_the_day = random.choice(quotes)

# send email -------------------------------
my_email = "user@email.com"
password = "password"

if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="user@email.com",
                            msg=f"Subject:Quote of the day\n\n{quote_of_the_day}")
        # connection.close()  # not necessary, closes automatically when using with ... as ...
