# Generated by Django 4.1.7 on 2023-04-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserTrips', '0005_publishedtrips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishedtrips',
            name='noOfDays',
        ),
    ]