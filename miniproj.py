import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")

# CITY="Thrissur"
CITY=input("Enter city name: ").strip()

url=f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


print("Requesting data from server...")

response=requests.get(url)

print("Status code:",response.status_code)


data=response.json()

city=data["name"]
temp=data["main"]["temp"]
feels_like=data["main"]["feels_like"]
humidity=data["main"]["humidity"]
pressure=data["main"]["pressure"]
weather_main=data["weather"][0]["main"]
description=data["weather"][0]["description"]
wind_speed=data["wind"]["speed"]

print("\n====== WEATHER REPORT ======")
print(f"City        : {city}")
print(f"Temperature : {temp} °C") 
print(f"Feels Like  : {feels_like} °C")
print(f"Humidity    : {humidity} %")
print(f"Pressure    : {pressure} hPa")
print(f"Condition   : {weather_main} ({description})")
print(f"Wind Speed  : {wind_speed} m/s")
print("============================")
# print("\nRaw JSON data:")
# print(data)