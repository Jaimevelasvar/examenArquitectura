# Generated by Django 4.2.2 on 2023-11-28 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_transaccion_cantidad_transaccion_destino_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='fechahora',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
