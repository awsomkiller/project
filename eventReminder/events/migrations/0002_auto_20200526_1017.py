# Generated by Django 3.0.6 on 2020-05-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtime',
            name='endTime',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='eventtime',
            name='startTime',
            field=models.CharField(default='', max_length=30),
        ),
    ]
