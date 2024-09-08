from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWeatherReminder.settings')

app = Celery('DjangoWeatherReminder')

# Load settings from Django settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all registered Django apps
app.autodiscover_tasks()

# Add periodic tasks
app.conf.beat_schedule = {
    'fetch-weather-every-hour': {
        'task': 'core.tasks.fetch_all_weather_data',
        'schedule': crontab(minute=0, hour='*'),  # Every hour
    },
    'cleanup-old-weather-data-every-day': {
        'task': 'core.tasks.cleanup_old_weather_data',
        'schedule': crontab(minute=0, hour=0),  # Every day at midnight
    },
}

#Configure timezone
app.conf.timezone = 'UTC'
