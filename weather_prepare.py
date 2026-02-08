import pandas as pd

df=pd.read_csv("weather_data.csv")

df["datetime"]=pd.to_datetime(df["date"]+" "+df["time"])

df=df.sort_values("datetime")

df=df[["datetime","city","temp"]]

df.to_csv("weather_clean.csv",index=False)

print("Cleaned data saved ✅")