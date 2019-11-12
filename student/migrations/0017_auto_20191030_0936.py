# Generated by Django 2.2.2 on 2019-10-30 09:36

import datetime
import django.core.validators
from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_questionbank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placed',
            name='year',
            field=models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1984), student.models.Placed.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 30, 9, 36, 58, 759834)),
        ),
    ]
