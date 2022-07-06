import requests
from datetime import datetime

MY_LAT = 45.419198
MY_LNG = -122.661495
# #Making a request to an API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# iss_position = (longitude,latitude)
# print(iss_position)
# #404 response code is the code that is given when what you look for does not exist

#Creating a dictionary to use as parameters for the API request below
parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}


#Copying sunset and sunrise time from an API
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.now()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise,sunset)
print(time_now.hour)