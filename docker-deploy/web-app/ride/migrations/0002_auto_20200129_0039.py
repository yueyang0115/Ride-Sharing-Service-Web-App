# Generated by Django 3.0.2 on 2020-01-29 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideowner',
            name='status',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
