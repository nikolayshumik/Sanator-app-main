# Generated by Django 4.2 on 2023-07-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_review_istochnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='istochnik',
            field=models.CharField(max_length=100),
        ),
    ]
