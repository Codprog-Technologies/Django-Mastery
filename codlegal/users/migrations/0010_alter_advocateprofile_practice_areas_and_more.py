# Generated by Django 5.0.2 on 2024-06-09 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointments", "0009_practicearea_insert_rows"),
        ("users", "0009_alter_advocateprofile_practice_areas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advocateprofile",
            name="practice_areas",
            field=models.ManyToManyField(
                related_name="advocate_profile_set",
                related_query_name="advocate_profile",
                to="appointments.practicearea",
            ),
        ),
        migrations.AlterField(
            model_name="advocateprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="advocate_profile",
                related_query_name="advocate_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="phonenumber",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phone_number_set",
                related_query_name="phone_number",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
