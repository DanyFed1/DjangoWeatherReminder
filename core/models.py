from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.country}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    notification_period = models.IntegerField()  # Period in hours (e.g., 1, 3, 6, 12)
    notify_via = models.CharField(max_length=50)  # e.g., 'email', 'webhook'
    webhook_url = models.CharField(max_length=255, null=True, blank=True)  # Only used if notify_via is 'webhook'
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_notified_at = models.DateTimeField(null=True, blank=True)  # Track when the last notification was sent

    def __str__(self):
        return f"{self.user.username} - {self.city.name} ({self.notification_period} hours)"

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    data = models.JSONField()  # Storing the weather data in JSON format
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather data for {self.city.name} at {self.fetched_at}"


