# Generated by Django 4.2.7 on 2023-11-30 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_transaccion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 20, 32, 56, 954173)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
