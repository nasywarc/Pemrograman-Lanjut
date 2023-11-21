import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "bb36f687e3df1168ca3299a08eb7fcb1"  # Ganti dengan kunci API OpenWeatherMap Anda
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        result = f"Temperature: {temperature}°C\nDescription: {description}"
        return result
    except Exception as e:
        return str(e)

def get_weather_report():
    city = city_entry.get()
    if city:
        weather_report = get_weather(city)
        result_label.config(text=weather_report)
    else:
        messagebox.showwarning("Warning", "Please enter a city.")

# GUI setup
app = tk.Tk()
app.title("Weather App")

# Widgets
label = tk.Label(app, text="Enter City:")
label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_report)
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the application
app.mainloop()
