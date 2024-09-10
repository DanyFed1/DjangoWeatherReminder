import requests
from django.utils import timezone
from dotenv import load_dotenv
from .models import City, WeatherData
import os

# Load environment variables from .env file
load_dotenv()

def fetch_weather_data(city, use_lat_lon=True):
    """Fetches weather data from OpenWeatherMap API for a given city."""
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')

    if use_lat_lon:
        # Fetch weather data using latitude and longitude
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={city.lat}&lon={city.lon}&appid={api_key}"
    else:
        # Fetch weather data using city name and country
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city.name},{city.country}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        WeatherData.objects.create(city=city, data=weather_data, fetched_at=timezone.now())
        return weather_data
    else:
        print(f"Failed to fetch weather data for {city.name}. Status code: {response.status_code}")
        return None
