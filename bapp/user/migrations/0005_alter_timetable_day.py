# Generated by Django 4.0 on 2022-04-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=1),
        ),
    ]