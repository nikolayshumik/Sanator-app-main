# Generated by Django 4.2 on 2023-07-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_remove_review_opros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО Должность')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Режим работы')),
                ('tel1', models.CharField(blank=True, max_length=100, null=True, verbose_name='телефон1')),
                ('tel2', models.CharField(blank=True, max_length=100, null=True, verbose_name='телефон2')),
                ('tel3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название3')),
            ],
        ),
    ]
