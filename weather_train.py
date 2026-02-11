import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv("weather_clean.csv")

models={}

for city in df["city"].unique():
    city_data=df[df["city"]==city]

    city_data["t"]=pd.to_datetime(city_data["datetime"]).astype("int64")//10**9

    X=city_data[["t"]]
    y=city_data["temp"]

    model=LinearRegression()
    model.fit(X,y)

    models[city]=model

joblib.dump(models,"weather_models.pkl")

print("Weather ML models trained ✅")