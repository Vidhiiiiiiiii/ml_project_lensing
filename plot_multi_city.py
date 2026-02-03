import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather_data.csv")
df["time"]=df["time"].str.replace("::",":",regex=False)
df["datetime"]=pd.to_datetime(df["date"]+" "+df["time"])

df=df.sort_values("datetime")

cities=df["city"].unique()

plt.figure()

for city in cities:
    city_data=df[df["city"]==city]
    plt.plot(city_data["datetime"],city_data["temp"],label=city)

plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends (All Cities)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()