# Generated by Django 2.2.2 on 2019-10-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20191018_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placed',
            name='year',
            field=models.CharField(default='2019', max_length=4),
        ),
    ]
