# Generated by Django 3.2.5 on 2021-07-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_management', '0004_merge_0002_auto_20210717_1648_0003_tripassign'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='stoppage_points',
            field=models.ManyToManyField(to='trip_management.Location'),
        ),
    ]
