# Generated by Django 4.1.6 on 2023-03-23 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 16, 51, 31, 81808, tzinfo=datetime.timezone.utc)),
        ),
    ]
