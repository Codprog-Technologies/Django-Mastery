# Generated by Django 5.0.2 on 2024-07-23 02:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PlatformReview",
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
                (
                    "satisfaction",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (5, "Very Satisfied"),
                            (4, "Satisfied"),
                            (3, "Neutral"),
                            (2, "Unsatisfied"),
                            (1, "Very Unsatisfied"),
                        ],
                        verbose_name="How satisfied are you with our Platform?",
                    ),
                ),
                ("description", models.TextField()),
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
