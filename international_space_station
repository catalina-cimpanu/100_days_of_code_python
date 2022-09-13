import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 48.13
MY_LONG = 11.50
MY_EMAIL = "user@email.com"
PASSWORD = "password"


# Your position is within +5 or -5 degrees of the ISS position.
def iss_is_near():
    # Get ISS position
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    iss_longitude = iss_data["iss_position"]["longitude"]
    iss_latitude = iss_data["iss_position"]["latitude"]

    if iss_longitude - 5 <= MY_LONG <= iss_longitude + 5 and iss_latitude - 5 <= MY_LAT <= iss_latitude + 5:
        return True
    else:
        return False


# get sunrise and sunset at my location
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# longer way
sunrise = data["results"]["sunrise"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunrise_min = sunrise.split("T")[1].split(":")[1]

# shorter way
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
sunset_min = data["results"]["sunset"].split("T")[1].split(":")[1]

hour_now = datetime.now().hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_dark():
    if int(sunset_hour) <= hour_now or hour_now <= int(sunrise_hour):
        return True
    else:
        return False

while True:
    time.sleep(300) # execute every 5 mins
    if is_dark() and iss_is_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="user@email.com",
                                msg=f"Subject:International Space Station is near!\n\nLook up! ☝ ISS is now over your city and you can see it")
    else:
        print("you can't see iss")
