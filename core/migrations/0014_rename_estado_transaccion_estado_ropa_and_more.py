# Generated by Django 4.2.7 on 2023-12-01 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_ingreso_transaccion_estado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaccion',
            old_name='estado',
            new_name='estado_ropa',
        ),
        migrations.RenameField(
            model_name='transaccion',
            old_name='tipo',
            new_name='tipo_transaccion',
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 21, 10, 21, 570974)),
        ),
    ]
