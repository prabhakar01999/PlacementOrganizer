# Generated by Django 2.2.2 on 2019-10-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20191017_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='certificateDescription',
            field=models.CharField(default='', max_length=50),
        ),
    ]