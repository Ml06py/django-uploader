# Generated by Django 4.0.3 on 2022-05-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_alter_userfile_file_alter_userfile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]