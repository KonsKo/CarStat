# Generated by Django 3.1.5 on 2021-01-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_car_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_create',
            field=models.DateTimeField(blank=True),
        ),
    ]