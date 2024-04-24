# Generated by Django 5.0.1 on 2024-01-13 11:31

import django.utils.timezone
import tictac.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TicTacToe",
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
                    "room_code",
                    models.CharField(
                        max_length=100, validators=[tictac.models.validate_room_code]
                    ),
                ),
                ("game_creator", models.CharField(max_length=100)),
                (
                    "game_opponent",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("is_over", models.BooleanField(default=False)),
                ("winner", models.CharField(blank=True, max_length=100, null=True)),
                ("dated", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]