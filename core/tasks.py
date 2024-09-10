from celery import shared_task
from .models import City, WeatherData
from django.utils import timezone
from datetime import timedelta
from .services import fetch_weather_data
from django.core.mail import send_mail
from .models import Subscription, WeatherData
import requests
from DjangoWeatherReminder.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

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

def should_notify(subscription):
    last_notified_at = subscription.last_notified_at or timezone.now() - timedelta(hours=subscription.notification_period)
    return timezone.now() >= last_notified_at + timedelta(hours=subscription.notification_period)

@shared_task
def send_weather_notifications():
    subscriptions = Subscription.objects.filter(active=True)
    for subscription in subscriptions:
        if should_notify(subscription):
            latest_weather = WeatherData.objects.filter(city=subscription.city).order_by('-fetched_at').first()
            if latest_weather:
                if subscription.notify_via == 'email':
                    send_email_notification(subscription, latest_weather)
                elif subscription.notify_via == 'webhook':
                    send_webhook_notification(subscription, latest_weather)

                # Update last notified timestamp
                subscription.last_notified_at = timezone.now()
                subscription.save()

def send_email_notification(subscription, weather_data):
    subject = f"Weather update for {subscription.city.name}"
    context = {
        'city_name': subscription.city.name,
        'weather_data': weather_data.data,
    }
    message = render_to_string('emails/weather_update_email.html', context)
    send_mail(subject, message, EMAIL_HOST_USER, [subscription.user.email], html_message=message)


def send_webhook_notification(subscription, weather_data):
    payload = {
        'city': subscription.city.name,
        'weather_data': weather_data.data
    }
    try:
        requests.post(subscription.webhook_url, json=payload)
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook for {subscription.user.username}: {e}")

