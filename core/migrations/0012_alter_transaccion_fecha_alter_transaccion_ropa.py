# Generated by Django 4.2.7 on 2023-11-30 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_transaccion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 20, 49, 42, 165718)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='ropa',
            field=models.CharField(default='', max_length=20),
        ),
    ]