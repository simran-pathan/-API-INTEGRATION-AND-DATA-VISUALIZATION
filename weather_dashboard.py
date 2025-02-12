import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Fetching data from Weathrbit API
API_KEY = "5038b52e33504ea8919ac2cb9c24b352"  
BASE_URL = "https://api.weatherbit.io/v2.0/forecast/daily"
#Asking user to enter the city for which they want to fetch the weather details
city = input("Enter the city you want:")


#Fetching the required data from the API
country = "IN"
params = {
    "city": city,
    "country": country,
    "key": API_KEY
}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    print("Data fetched successfully!")
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

#Creating the Dashboard for the required weather details
forecast_data = data["data"]
df = pd.DataFrame(forecast_data)

df["datetime"] = pd.to_datetime(df["datetime"])
df.set_index("datetime", inplace=True)

df = df[["temp", "max_temp", "min_temp", "precip", "wind_spd"]]

sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(df.index, df["temp"], label="Avg Temp (°C)", color="orange", marker="o",linestyle = '-.')
plt.fill_between(df.index, df["min_temp"], df["max_temp"], color="lightblue", alpha=0.5, label="Min-Max Range")
plt.title(f"Weather Forecast for {city.capitalize()}")
plt.ylabel("Temperature (°C)")
plt.xlabel("Date")
plt.yticks(rotation = 45)
plt.xticks(rotation = 300)
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(df.index, df["precip"], color="pink", alpha=0.7, label="Precipitation (mm)")
plt.plot(df.index, df["wind_spd"], color="green", marker="x", label="Wind Speed (m/s)", linewidth=2,linestyle = '-.')
plt.ylabel("Precipitation / Wind Speed")
plt.xlabel("Date")
plt.xticks(rotation = 300)
plt.yticks(rotation=45)
plt.legend()

#Displaying the Dashboard
plt.tight_layout()
plt.show()
