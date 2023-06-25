from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django import forms


# class UserDailySchedule(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     weekday = models.CharField(max_length=10)
#     schedule = models.TextField()
#
#     def __str__(self):
#         return f'{self.weekday} - {self.user.username}'

class UserDailySchedule(models.Model):
    WEEKDAY_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=200,  null=True)
    weekday = models.CharField(max_length=11, choices=WEEKDAY_CHOICES)
    start_time = models.DateTimeField(default=datetime.datetime(2023, 6, 21, 0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0), blank=True, null=True)
    description = models.TextField( null=True)

    def str(self):
        return self.schedule
# class UserDailySchedule(models.Model):
#     WEEKDAY_CHOICES = (
#         ('понедельник', 'Понедельник'),
#         ('вторник', 'Вторник'),
#         ('среда', 'Среда'),
#         ('четверг', 'Четверг'),
#         ('пятница', 'Пятница'),
#         ('суббота', 'Суббота'),
#         ('воскресенье', 'Воскресенье'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     schedule = models.CharField(max_length=200, blank=True, null=True)
#     weekday = models.CharField(max_length=11, choices=WEEKDAY_CHOICES)
#     start_time = models.DateTimeField(default=datetime.datetime(2023, 6, 21, 0, 0))
#     end_time = models.TimeField(default=datetime.time(0, 0))
#     description = models.TextField(blank=True, null=True)
#
#     def str(self):
#         return self.schedule



class Rools(models.Model):
    title = models.CharField('Название', max_length=300)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'


class Rasporiadok(models.Model):
    title = models.CharField('Название', max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Распорядок дня'
        verbose_name_plural = 'Распорядок дней'


class Posters(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='posters/', default='default.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афиши'
        
class Zapret(models.Model):
    title = models.CharField('Название', max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрет'
        verbose_name_plural = 'Запреты'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.user.username} {self.user.last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        unique=True
    )
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f" {self.user.username} {self.user.first_name} {self.user.last_name}"

class Scheduledaily(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=200)

    WEEKDAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday')
    ]

    weekday = models.IntegerField(choices=WEEKDAY_CHOICES)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('day', 'start_time')


