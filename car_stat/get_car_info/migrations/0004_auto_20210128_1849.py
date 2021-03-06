# Generated by Django 3.1.5 on 2021-01-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_car_info', '0003_auto_20210128_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclegeneration',
            name='brand',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='get_car_info.vehiclebrand'),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='get_car_info.vehiclebrand'),
        ),
    ]
