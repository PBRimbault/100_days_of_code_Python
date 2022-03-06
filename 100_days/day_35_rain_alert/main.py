import requests
from twilio.rest import Client

api_key = "2bc48a7f4fa1751da380c3f3e9949cdb"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'ACc50768f767887369eba0020f64a6b7d5'
auth_token = '85a977d2f2a45d71a22618f7d2ee3a89'

# Cape Town, South Africa
MY_LAT = -33.924870
MY_LNG = 18.424055

# # Montenegro, Brazil
# MY_LAT = -29.689230
# MY_LNG = -51.467060

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": 'current,minutely,daily',
    "appid": api_key
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

data = response.json()
hourly_weather = data['hourly']


def check_for_rain():
    will_rain = False

    for hour in hourly_weather[:11]:
        if int(hour['weather'][0]['id']) < 700 and will_rain == False:
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body="Bring and umbrealla today - it's going to rain",
                     from_='+17047033036',
                     to='+27716067067'
                 )

            print(message.status)
            will_rain = True

check_for_rain()