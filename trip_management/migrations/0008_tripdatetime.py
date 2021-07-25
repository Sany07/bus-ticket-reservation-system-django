# Generated by Django 3.2.5 on 2021-07-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_management', '0007_tripassign_fleet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripDateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'TripDateTime',
                'verbose_name_plural': 'TripDateTimes',
            },
        ),
    ]
