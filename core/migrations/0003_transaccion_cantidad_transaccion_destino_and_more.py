# Generated by Django 4.2.2 on 2023-11-28 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_transaccion_remove_ropa_talla'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='destino',
            field=models.CharField(default='hospital', max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='fechahora',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='ingreso',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='limpia',
            field=models.BooleanField(default=True),
        ),
    ]