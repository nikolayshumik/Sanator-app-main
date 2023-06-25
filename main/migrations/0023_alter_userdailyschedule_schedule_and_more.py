# Generated by Django 4.2 on 2023-06-21 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_scheduledaily_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdailyschedule',
            name='schedule',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdailyschedule',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 21, 0, 0)),
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]