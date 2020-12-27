# Generated by Django 2.2.12 on 2020-12-27 06:16

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('thumbnail', models.TextField()),
                ('venue', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('totalregisters', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]