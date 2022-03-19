import requests
import smtplib
my_email = "babatundeibukun981@gmail.com"
my_password = "input your password"

api_key = "c155be81e86ffb11b8a8d6e7134bf654"
parameters = {"lat": 9.081999,
              "lon": 8.675277,
              "appid": api_key,
              "exclude": "current,minutely,daily"
              }
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
list_weather = []
will_rain = False
for i in range(0, 12):
    weather_condition = data["hourly"][i]["weather"][0]["id"]
    list_weather.append(weather_condition)
    for i in list_weather:
        if i < 700:
            will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.sendmail(from_addr=my_email, to_addrs="babatundeibukundavid@gmail.com",
                            msg="subject:RAIN DAY\n\nTake an umbrella , it going to rain ")
