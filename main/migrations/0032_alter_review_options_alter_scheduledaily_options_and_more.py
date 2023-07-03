# Generated by Django 4.2 on 2023-06-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_posters_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='scheduledaily',
            options={'ordering': ('день', 'времяначала')},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.RenameField(
            model_name='scheduledaily',
            old_name='start_time',
            new_name='времяначала',
        ),
        migrations.RenameField(
            model_name='scheduledaily',
            old_name='end_time',
            new_name='времяокончания',
        ),
        migrations.RenameField(
            model_name='scheduledaily',
            old_name='day',
            new_name='день',
        ),
        migrations.RenameField(
            model_name='scheduledaily',
            old_name='description',
            new_name='описание',
        ),
        migrations.RenameField(
            model_name='scheduledaily',
            old_name='user',
            new_name='пользователь',
        ),
        migrations.RenameField(
            model_name='userdailyschedule',
            old_name='start_time',
            new_name='время_начала',
        ),
        migrations.RenameField(
            model_name='userdailyschedule',
            old_name='end_time',
            new_name='время_окончания',
        ),
        migrations.RenameField(
            model_name='userdailyschedule',
            old_name='description',
            new_name='описание',
        ),
        migrations.RenameField(
            model_name='userdailyschedule',
            old_name='user',
            new_name='пользователь',
        ),
        migrations.RenameField(
            model_name='userdailyschedule',
            old_name='schedule',
            new_name='расписание',
        ),
        migrations.RemoveField(
            model_name='scheduledaily',
            name='weekday',
        ),
        migrations.RemoveField(
            model_name='userdailyschedule',
            name='weekday',
        ),
        migrations.AddField(
            model_name='scheduledaily',
            name='деньнедели',
            field=models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], default=0),
        ),
        migrations.AddField(
            model_name='userdailyschedule',
            name='деньнедели',
            field=models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], default=0),
        ),
        migrations.AlterField(
            model_name='posters',
            name='image',
            field=models.ImageField(default='default.png', upload_to='posters/', verbose_name='Изображение'),
        ),
    ]
