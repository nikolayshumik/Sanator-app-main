# Generated by Django 4.2 on 2023-07-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_услуга'),
    ]

    operations = [
        migrations.AddField(
            model_name='услуга',
            name='дополнительная_информация',
            field=models.TextField(blank=True, null=True),
        ),
    ]
