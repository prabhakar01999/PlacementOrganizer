# Generated by Django 2.2.2 on 2019-10-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_certificates_hallticketnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='presentBacklogs',
            field=models.IntegerField(default=0),
        ),
    ]