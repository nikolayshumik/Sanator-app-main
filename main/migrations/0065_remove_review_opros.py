# Generated by Django 4.2 on 2023-07-05 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_alter_услуга_ваше_назв_alter_услуга_название'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='opros',
        ),
    ]
