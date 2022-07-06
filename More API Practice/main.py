import requests
import os
from twilio.rest import Client

account_sid : str #<input your sid here>
auth_token: str #<input your auth_token here>
api_key: str #<input api_key>

parameters = {
    "lat":-18.9137,
    "lon":47.5361,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
data.raise_for_status()
json_data = data.json()
# print(json_data['hourly'][0]['weather'][0]['id'])
weather_slice = json_data['hourly'][:12] # takes the first 11 hours of the day

will_rain = False
for hour in weather_slice:
    if int(hour['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
    .create(
    body="Bring an umbrella, it will rain today",
    from_="+19379155904",
    to="+261329375832"
    )
    print(message.status)
