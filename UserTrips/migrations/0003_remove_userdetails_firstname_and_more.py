# Generated by Django 4.1.7 on 2023-04-09 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserTrips', '0002_alter_userdetails_user_preferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='lastName',
        ),
    ]
