# Generated by Django 4.2.7 on 2023-11-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_transaccion_ingreso_alter_transaccion_limpia'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='ropa',
            field=models.CharField(default='', max_length=10),
        ),
    ]
