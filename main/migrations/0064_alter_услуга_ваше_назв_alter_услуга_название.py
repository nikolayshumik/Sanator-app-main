# Generated by Django 4.2 on 2023-07-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_услуга_ваше_назв'),
    ]

    operations = [
        migrations.AlterField(
            model_name='услуга',
            name='ваше_назв',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='услуга',
            name='название',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
