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

# class UserDailySchedule(models.Model):
#     WEEKDAY_CHOICES = (
#         ('Понедельник', 'Понедельник'),
#         ('Вторник', 'Вторник'),
#         ('Среда', 'Среда'),
#         ('Четверг', 'Четверг'),
#         ('Пятница', 'Пятница'),
#         ('Суббота', 'Суббота'),
#         ('Воскресенье', 'Воскресенье'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     schedule = models.CharField(max_length=200,  null=True)
#     weekday = models.CharField(max_length=11, choices=WEEKDAY_CHOICES)
#     start_time = models.DateTimeField(default=datetime.datetime(2023, 6, 21, 0, 0))
#     end_time = models.TimeField(default=datetime.time(0, 0), blank=True, null=True)
#     description = models.TextField( null=True)
#
#     def str(self):
#         return self.schedule

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    goal_choice = models.CharField(max_length=50, choices=(
        ('', ''),
        ('лечение', 'Лечение'),
        ('оздоровление', 'Оздоровление'),
        ('отдых', 'Отдых'),
    ), default='', verbose_name="Цель выбора здравницы", null=True, blank=True)
    visit_choice = models.CharField(max_length=50, choices=(
        ('', ''),
        ('впервые', 'Впервые'),
        ('повторно', 'Повторно'),
        ('более двух раз', 'Более двух раз'),
    ), default='', verbose_name="Посещаете данную здравницу", null=True, blank=True)
    istochnik = models.CharField(max_length=100, verbose_name="Источник", null=True, blank=True)
    # istochnik = models.CharField(max_length=50, choices=(
    #     ('', ''),
    #     ('знакомые', 'Знакомые'),
    #     ('реклама', 'Реклама'),
    #     ('другой вариант', 'Другой вариант'),
    # ), default='', verbose_name="Источник получения информации")
    kak_preobletali = models.CharField(max_length=50, choices=(
        ('', ''),
        ('полная стоимость', 'Полная стоимость'),
        ('льготная стоимость', 'Льготная стоимость'),
    ), default='', verbose_name="Как приобретали путевку", null=True, blank=True)
    gruppa = models.CharField(max_length=50, choices=(
        ('', ''),
        ('не имею', 'не имею'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ), default='', verbose_name="Группа ограничений трудоспособности", null=True, blank=True)
    treatment_rating = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества лечения", null=True, blank=True)
    service_rating = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества сервиса", null=True, blank=True)
    projivanie = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества проживания", null=True, blank=True)
    pitanie = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества питания", null=True, blank=True)
    soc_deatel= models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества социокультурной деятельности", null=True, blank=True)
    kval_med_pers = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка качества квалификации медицинского персонала", null=True, blank=True)
    vrach = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка культуры обслуживания врачей", null=True, blank=True)
    sred_med = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка культуры обслуживания среднего медицинского персонала", null=True, blank=True)
    obsluj = models.CharField(max_length=50, choices=(
        ('', ''),
        ('1', '1 - Плохо'),
        ('2', '2 - Удовлетворительно'),
        ('3', '3 - Хорошо'),
        ('4', '4 - Очень хорошо'),
        ('5', '5 - Отлично'),
    ), default='', verbose_name="Оценка культуры обсуживающего персонала", null=True, blank=True)
    kak_v_celom = models.CharField(max_length=50, choices=(
        ('', ''),
        ('удовлетворительно', 'Удовлетворительно'),
        ('хорошо', 'Хорошо'),
        ('отлично', 'Отлично'),
    ), default='', verbose_name="Как в целом Вы можете оценить впечатления от пребывания в санатории", null=True, blank=True)
    kakova_ver = models.CharField(max_length=50, choices=(
        ('', ''),
        ('0', 'ни в коем случае'),
        ('1', 'Вряд ли'),
        ('2', 'Возможно'),
        ('3', 'Скорее всего да'),
        ('4', 'Расскажу конечно'),
        ('5', 'обязательно порекомендую'),
    ), default='', verbose_name="Какова вероятность что вы порекомендуете данную здравницу друзьям", null=True, blank=True)
    opros = models.CharField(max_length=50, choices=(
        ('', ''),
        ('0', 'ни в коем случае'),
        ('1', 'Вряд ли'),
        ('2', 'Возможно'),
        ('3', 'Скорее всего да'),
        ('4', 'Расскажу конечно'),
        ('5', 'обязательно порекомендую'),
    ), default='', verbose_name="Какова вероятность что вы порекомендуете данную здравницу друзьям", null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", default=0, null=True,blank=True)
    gender = models.CharField(max_length=1, choices=(('м', 'М'), ('ж', 'Ж'), ('', '')), verbose_name="Пол", default='', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name="Город", default='', null=True, blank=True)
    text = models.TextField(verbose_name="отзыв", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата")
    # istochnik = models.CharField(max_length=50, choices=(
    #     ('', ''),
    #     ('знакомые', 'Знакомые'),
    #     ('реклама', 'Реклама'),
    #     ('другой вариант', 'Другой вариант'),
    # ), default='')
    def __str__(self):
        return f"Отзыв от {self.user.username} {self.user.last_name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        unique=True
    )
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f" {self.user.username} {self.user.first_name} {self.user.last_name}"

# class Scheduledaily(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     day = models.IntegerField()
#     start_time = models.TimeField()
#     end_time = models.TimeField(blank=True, null=True)
#     description = models.CharField(max_length=200)
#
#     WEEKDAY_CHOICES = [
#         (0, 'Monday'),
#         (1, 'Tuesday'),
#         (2, 'Wednesday'),
#         (3, 'Thursday'),
#         (4, 'Friday'),
#         (5, 'Saturday'),
#         (6, 'Sunday')
#     ]
#
#     weekday = models.IntegerField(choices=WEEKDAY_CHOICES)
#
#     def __str__(self):
#         return self.description
#
#     class Meta:
#         ordering = ('day', 'start_time')
class Scheduledaily(models.Model):
    пользователь = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    день = models.IntegerField()
    времяначала = models.TimeField()
    времяокончания = models.TimeField(blank=True, null=True)
    описание = models.CharField(max_length=200)

    ДНИНЕДЕЛИ = [
        ('понедельник', 'Понедельник'),
        ('вторник', 'Вторник'),
        ('среда', 'Среда'),
        ('четверг', 'Четверг'),
        ('пятница', 'Пятница'),
        ('суббота', 'Суббота'),
        ('воскресенье', 'Воскресенье')
    ]

    деньнедели = models.CharField(max_length=20, choices=ДНИНЕДЕЛИ, default='понедельник')

    def str(self):
        return self.описание

    class Meta:
        ordering = ('день', 'времяначала')


class Личноерасписание(models.Model):
    # было ДНИ_НЕДЕЛИ
    ДНИНЕДЕЛИ = [
        ('понедельник', 'Понедельник'),
        ('вторник', 'Вторник'),
        ('среда', 'Среда'),
        ('четверг', 'Четверг'),
        ('пятница', 'Пятница'),
        ('суббота', 'Суббота'),
        ('воскресенье', 'Воскресенье')
    ]

    пользователь = models.ForeignKey(User, on_delete=models.CASCADE)
    расписание = models.CharField(max_length=200, null=True)
    деньнедели = models.CharField(max_length=20, choices=ДНИНЕДЕЛИ, default='понедельник')
    время_начала = models.DateTimeField(default=datetime.datetime(2023, 6, 21, 0, 0))
    время_окончания = models.TimeField(default=datetime.time(0, 0), blank=True, null=True)
    описание = models.TextField(null=True)

    def __str__(self):
        return f'{self.пользователь} {self.пользователь.last_name} {self.деньнедели}'

    class Meta:
        verbose_name = 'Личное расписание'
        verbose_name_plural = 'Личное расписание'


class Услуга(models.Model):
    номер = models.IntegerField(blank=True, null=True)
    название = models.CharField(max_length=300, blank=True, null=True)
    описание = models.TextField(blank=True, null=True)
    ед_измерения = models.CharField(max_length=50, blank=True, null=True)
    цена = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    дополнительная_информация = models.TextField(blank=True, null=True)
    ваше_назв = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        номер = str(self.номер) if self.номер is not None else ""
        название = self.название if self.название is not None else ""

        if self.ваше_назв is not None:
            return self.ваше_назв
        else:
            return f'{номер} {название}'

class Feedback(models.Model):
    CHOICES = (
        ('лечение', 'Лечение'),
        ('оздоровление', 'Оздоровление'),
        ('отдых', 'Отдых'),
    )

    goal_choice = models.CharField(max_length=50, choices=CHOICES)
    comment = models.TextField()
