# Generated by Django 4.2.5 on 2023-12-18 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_atencion_fecha_y_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='fecha_y_hora',
        ),
        migrations.AddField(
            model_name='atencion',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='atencion',
            name='hora',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
