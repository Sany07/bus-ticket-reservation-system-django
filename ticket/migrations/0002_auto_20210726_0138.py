# Generated by Django 3.2.5 on 2021-07-26 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0008_auto_20210726_0031'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketprice',
            name='fleet_type',
        ),
        migrations.AddField(
            model_name='ticketprice',
            name='fleet_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fleet_management.fleettype'),
            preserve_default=False,
        ),
    ]
