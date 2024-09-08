from rest_framework import serializers
from .models import City, Subscription, WeatherData

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Subscription
        fields = ['id', 'city', 'notification_period', 'notify_via', 'webhook_url', 'active']

class WeatherDataSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = WeatherData
        fields = ['city', 'data', 'fetched_at']
