# Generated by Django 4.2.2 on 2023-11-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='ropa',
            name='talla',
        ),
    ]
