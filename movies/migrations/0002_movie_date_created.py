# Generated by Django 3.0.8 on 2020-08-01 21:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
