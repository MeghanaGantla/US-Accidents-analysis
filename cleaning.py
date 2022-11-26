import pandas as pd

df = pd.read_csv("US_Accidents_Dec21_updated.csv")


df.drop(["ID", "End_Lat", "End_Lng", "Description", "Side", "Zipcode", "Country", "Weather_Timestamp", "Civil_Twilight",
         "Nautical_Twilight", "Astronomical_Twilight"], axis=1)
print(df.columns)

df.to_csv("US_Accidents_Nov22.csv")