import pandas as pd
df=pd.read_csv("weather_data.csv")

# print("\n==== FIRST 5 ROWS ====")
# print(df.head())

# print("\n==== LAST 5 ROWS ====")
# print(df.tail())

# print("\n==== DATA INFO ====")
# print(df.info())

# print("\n==== STATISTICS ====")
# print(df.describe())

# print("\n==== COUMN NAMES ====")
# print(df.columns)

print("\n==== CITY-WISE SUMMARY ====")

city_group=df.groupby("city")

print(city_group[["temp","humidity","wind_speed"]].mean())
print(city_group[["temp","humidity","wind_speed"]].max())
print(city_group[["temp","humidity","wind_speed"]].min())

print("\n==== DATA COUNT PER CITY ====")
print(df["city"].value_counts())
