# Generated by Django 5.0.2 on 2024-03-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
