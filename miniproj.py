import requests
# API_KEY="d71942627babc7caad0c8c9552c89081"
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")

CITY="Delhi"

url=f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


print("Requesting data from server...")

response=requests.get(url)

print("Status code:",response.status_code)


data=response.json()
# print("Raw response text:")
# print(response.text)
# print("Status code:",response.status_code)
print("\nRaw JSON data:")
print(data)