import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
API_KEY = os.environ.get("OWM_API_KEY")

lat = 33.684422
lon = 73.047882

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&cnt=4"
)
response.raise_for_status()
weather_data = response.json()

gonna_rain = False

for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        gonna_rain = True

if gonna_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an umbrella :)",
        from_="+18563721945",
        to="+923265147157"
    )
    print(message.status)