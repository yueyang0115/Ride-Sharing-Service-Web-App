# Generated by Django 3.0.2 on 2020-01-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0006_auto_20200131_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideowner',
            name='driver_license',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rideowner',
            name='driver_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
