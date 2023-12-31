# Generated by Django 4.2.2 on 2023-12-01 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_transaccion_fechahora_transaccion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='destino',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='ingreso',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='limpia',
            field=models.BooleanField(),
        ),
    ]
