# Generated by Django 2.2.2 on 2019-10-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20191017_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='sem7Completed',
            field=models.CharField(choices=[('completed', 'completed'), ('stillBacklog', 'stillBacklog'), ('not-yet', 'not-yet')], default='No', max_length=7),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='sem8Completed',
            field=models.CharField(choices=[('completed', 'completed'), ('stillBacklog', 'stillBacklog'), ('not-yet', 'not-yet')], default='No', max_length=7),
        ),
    ]
