# Generated by Django 2.2.2 on 2019-10-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]