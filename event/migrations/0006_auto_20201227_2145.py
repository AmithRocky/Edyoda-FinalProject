# Generated by Django 2.2.12 on 2020-12-27 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_remove_event_totalregisters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
