# Generated by Django 2.2.2 on 2019-10-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20191018_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('companyEmail', models.CharField(max_length=50)),
                ('exam_date', models.DateField()),
            ],
        ),
    ]
