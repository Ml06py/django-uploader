# Generated by Django 4.0.3 on 2022-04-05 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='expiration',
        ),
    ]
