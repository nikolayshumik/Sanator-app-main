# Generated by Django 4.2 on 2023-07-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_remove_review_rating_alter_review_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='gender',
            field=models.CharField(blank=True, choices=[('м', 'М'), ('ж', 'Ж'), ('', '')], default='', max_length=1, null=True, verbose_name='Пол'),
        ),
    ]
