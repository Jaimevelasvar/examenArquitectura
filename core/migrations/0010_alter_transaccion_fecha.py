# Generated by Django 4.2.7 on 2023-11-30 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_transaccion_fecha_alter_transaccion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 20, 34, 53, 429797)),
        ),
    ]
