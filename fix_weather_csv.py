import pandas as pd

FILE="weather_data.csv"

df=pd.read_csv(FILE)

df["time"]=df["time"].str.replace("::",":",regex=False)

df.to_csv(FILE,index=False)

print("Fixed CSV saved as weather_data_fixed.csv ✅")