# Generated by Django 4.2.14 on 2024-09-01 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("lat", models.FloatField()),
                ("lon", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.JSONField()),
                ("fetched_at", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.city"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notification_period", models.IntegerField()),
                ("notify_via", models.CharField(max_length=50)),
                (
                    "webhook_url",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.city"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
