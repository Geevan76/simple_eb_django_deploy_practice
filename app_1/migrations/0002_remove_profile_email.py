# Generated by Django 5.2 on 2025-04-11 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
