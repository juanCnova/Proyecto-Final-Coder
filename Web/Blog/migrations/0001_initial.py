# Generated by Django 4.1.6 on 2023-03-23 16:46

import datetime
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
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime(2023, 3, 23, 13, 46, 4, 638667))),
                ('titulo', models.CharField(max_length=20)),
                ('subTitulo', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
