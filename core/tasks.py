from celery import shared_task
from .models import City, WeatherData
from django.utils import timezone
from datetime import timedelta
from .services import fetch_weather_data

@shared_task
def fetch_all_weather_data():
    """Fetch weather data for all cities in the database."""
    cities = City.objects.all()
    for city in cities:
        fetch_weather_data(city)

@shared_task
def cleanup_old_weather_data():
    """Remove weather data that's older than 24 hours."""
    yesterday = timezone.now() - timedelta(days=1)
    WeatherData.objects.filter(fetched_at__lt=yesterday).delete()
