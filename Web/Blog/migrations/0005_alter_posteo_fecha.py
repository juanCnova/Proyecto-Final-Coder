# Generated by Django 4.1.6 on 2023-03-23 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_posteo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
