# import requests
# import csv
# import time
# from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY=os.getenv("API_KEY")

# CITIES=["Thrissur","Jalandhar","Dubai"]

# FILE="weather_data.csv"

# def fetch_weather(city):
#     url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     res=requests.get(url)
#     data=res.json()

#     if data["cod"] != 200:
#         print("Error fetching data for",city)
#         return 
    
#     now=datetime.now()

#     row=[
#         now.strftime("%Y-%m-%d"),
#         now.strftime("%H:%M::%S"),
#         city,
#         data["main"]["temp"],
#         data["main"]["feels_like"],
#         data["main"]["humidity"],
#         data["main"]["pressure"],
#         data["wind"]["speed"],
#         data["weather"][0]["main"]

#     ]

#     with open(FILE,"a",newline="") as f:
#         writer=csv.writer(f)
#         writer.writerow(row)

#     print("Saved:",city,data["main"]["temp"],"°C at",now.strftime("%H:%M:%S"))

# while True:
#     print("\n==== Fetching Weather Data ====")

#     for city in CITIES:
#         fetch_weather(city)
        
#     print("Waiting ...\n")
#     time.sleep(30)