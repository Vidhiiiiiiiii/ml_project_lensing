import pandas as pd
import joblib
import matplotlib.pyplot as plt
from datetime import timedelta

df=pd.read_csv("weather_clean.csv")
df["datetime"]=pd.to_datetime(df["datetime"])
models=joblib.load("weather_models.pkl")

city=input("Enter city name: ")

city_data=df[df["city"]==city]

if len(city_data)==0:
    print("City not found ❌")
    exit()

latest=city_data.iloc[-1]

current_temp=latest["temp"]
current_time=pd.to_datetime(latest["datetime"])

next_time=current_time+timedelta(hours=1)

t=int(next_time.timestamp())

pred=models[city].predict([[t]])[0]


print("\n📍 City:",city)
print("🌡️ Current Temp:",round(current_temp,2),"°C")
print("📈 Next Hour Prediction:",round(pred,2),"°C")

print("📊 Avg:",round(city_data['temp'].mean(),2))
print("🔥 Max:",round(city_data['temp'].max(),2))
print("❄️ Min:",round(city_data['temp'].min(),2))

plt.figure()

plt.plot(city_data["datetime"],city_data["temp"],label="Past Data")

plt.scatter(next_time,pred,color="red",label="Prediction")

plt.legend()
plt.xticks(rotation=45)
plt.title(f"Weather Dashboard: {city}")
plt.tight_layout()
plt.show()
