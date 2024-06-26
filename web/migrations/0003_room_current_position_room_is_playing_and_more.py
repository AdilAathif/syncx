# Generated by Django 4.2.7 on 2024-04-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_room_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_position',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='room',
            name='is_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='total_length',
            field=models.FloatField(default=0.0),
        ),
    ]
