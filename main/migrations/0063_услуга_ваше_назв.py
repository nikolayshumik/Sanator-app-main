# Generated by Django 4.2 on 2023-07-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_alter_услуга_описание'),
    ]

    operations = [
        migrations.AddField(
            model_name='услуга',
            name='ваше_назв',
            field=models.TextField(blank=True, null=True),
        ),
    ]
