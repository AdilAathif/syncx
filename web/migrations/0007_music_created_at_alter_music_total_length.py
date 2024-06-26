# Generated by Django 4.2.7 on 2024-04-23 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_music_total_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='total_length',
            field=models.FloatField(default=0.0),
        ),
    ]
