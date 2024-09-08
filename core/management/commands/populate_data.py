from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import City, Subscription, WeatherData
from django.utils import timezone


class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Create user
        user, created = User.objects.get_or_create(
            username="Daniil Fjodorov",
            email="daniil.fjodorov@gmail.com",
            defaults={"password": "test_user"}
        )

        # Create cities
        cities_data = [
            {"name": "London", "country": "UK", "lat": 51.5085, "lon": -0.1257},
            {"name": "Amsterdam", "country": "NL", "lat": 52.3676, "lon": 4.9041},
        ]

        cities = []
        for city_data in cities_data:
            city, created = City.objects.get_or_create(
                name=city_data["name"],
                country=city_data["country"],
                lat=city_data["lat"],
                lon=city_data["lon"],
            )
            cities.append(city)

        # Create subscription for user
        for city in cities:
            Subscription.objects.get_or_create(
                user=user,
                city=city,
                notification_period=1,  # Every hour
                notify_via="email",
                active=True
            )

        # Print result
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data!'))
