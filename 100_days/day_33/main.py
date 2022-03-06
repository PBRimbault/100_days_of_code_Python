import requests
from datetime import datetime
import smtplib

my_email = "patrick.rimbault@gmail.com"
password = "szibuwnbjefidhne"

MY_LAT = -33.924870
MY_LNG = 18.424055
TOLERANCE = 5

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

# Your positions is within +5 or -5 degrees of the ISS position

my_position = {
    'lat' : MY_LAT,
    'lng' : MY_LNG,
    'formatted' : 0,
}

# If the ISS is close to my current position

def check_position():
    if my_position['lat'] < iss_latitude + TOLERANCE and my_position['lat'] > iss_latitude - TOLERANCE:
        if my_position['lng'] < iss_longitude + TOLERANCE and my_position['lng'] > iss_longitude - TOLERANCE:
            return True
    else:
        return False

response = requests.get("https://api.sunrise-sunset.org/json", params=my_position)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# and it is currently dark

def check_dark():
    if time_now > sunset or time_now < sunrise:
        return True
    else:
        return False

# Then send me an email to tell me to look up
message = f"The time is: {datetime.now()}\nSunset is: {data['results']['sunrise']}\nSunrise is: {data['results']['sunset']}\nThe ISS postion is: Latitude: {iss_latitude}, Longitude: {iss_longitude}\nYour position is: Latitude: {my_position['lat']}, Longitude: {my_position['lng']}"

if check_dark() and check_position():
    with smtplib.SMTP("smtp.gmail.com") as connection:            
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Look up!\n\nThe International Space Station is overhead, look up to the sky and see if you can see it.\n{message}"
                )
elif check_dark():
    print(f"It's dark, but the ISS isn't overhead\n{message}")
elif check_position():
    print(f"The ISS is overhead, but it isn't dark outside\n{message}")
else:
    print(f"The ISS not overhead and it isn't dark outside\n{message}")
# BONUS: run the code every 60 seconds