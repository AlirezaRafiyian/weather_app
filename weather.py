import requests
from geopy.geocoders import Nominatim

def get_lat_lon(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def get_weather(lat, lon, api_key):
    base_url = "https://api.openweathermap.org/data/3.0/onecall?"
    exclude = "minutely,hourly"  

    complete_url = f"{base_url}lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    if response.status_code == 401:
        return "Invalid API key"
    
    data = response.json()

    if "current" in data:
        current = data["current"]
        temperature = current["temp"]
        pressure = current["pressure"]
        humidity = current["humidity"]
        weather_description = current["weather"][0]["description"]

        weather_info = f"Temperature: {temperature}°C\n"
        weather_info += f"Pressure: {pressure} hPa\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Description: {weather_description}"

        return weather_info
    else:
        return "Weather data not found"
