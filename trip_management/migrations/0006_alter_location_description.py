# Generated by Django 3.2.5 on 2021-07-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_management', '0005_route_stoppage_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
