# Generated by Django 5.0.2 on 2024-02-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointments", "0002_alter_practicearea_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="practicearea",
            name="name",
            field=models.CharField(max_length=25, verbose_name="Name of Law"),
        ),
    ]
