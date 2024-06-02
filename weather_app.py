import tkinter as tk
from tkinter import messagebox
from weather import get_lat_lon, get_weather

api_key = "Your API" 

# Function to display weather data
def show_weather():
    city = city_entry.get()
    lat, lon = get_lat_lon(city)
    if lat is not None and lon is not None:
        weather_info = get_weather(lat, lon, api_key)
        if weather_info == "Invalid API key":
            messagebox.showerror("Error", "Invalid API key")
        elif weather_info == "Weather data not found":
            messagebox.showerror("Error", "Weather data not found")
        else:
            weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found")

# Creating main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#3498db")


title_label = tk.Label(root, text="Weather App", font=("Helvetica", 24, "bold"), bg="#3498db", fg="white")
title_label.pack(pady=10)


city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 14), bg="#3498db", fg="white")
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Helvetica", 14), width=20)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14), command=show_weather, bg="#2980b9", fg="white")
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#3498db", fg="white", wraplength=300, justify="left")
weather_label.pack(pady=10)


root.mainloop()
