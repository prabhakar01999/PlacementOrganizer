# Generated by Django 2.2.2 on 2019-10-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20191017_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='fatherGuardianAnnualIncome',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='motherAnnualIncome',
            field=models.IntegerField(default=0),
        ),
    ]
