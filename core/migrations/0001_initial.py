# Generated by Django 4.2.2 on 2023-11-28 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('talla', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
