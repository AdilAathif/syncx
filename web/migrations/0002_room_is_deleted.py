# Generated by Django 5.0.4 on 2024-04-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
