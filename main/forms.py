from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review
from .models import UserProfile
from django.contrib.auth import get_user_model
from main.models import UserProfile
from django.forms import ModelForm
from .models import Posters
from .models import Feedback
from django.core.exceptions import ValidationError


class ImageForm(ModelForm):
    class Meta:
        model = Posters
        fields = ['title', 'description', 'image']

class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(max_length=30, required=True, label='Фамилия')
    phone_number = forms.CharField(max_length=30, required=True, label='Номер телефона')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Повторите пароль')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.last_name = self.cleaned_data['last_name']
        phone_number = self.cleaned_data['phone_number']
        user.set_password(self.cleaned_data['password1'])
        user.save()

        if commit:
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                phone_number=phone_number
            )

        return user
    class Meta:
        model = User
        fields = ('username', 'last_name', 'phone_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ReviewForm(forms.ModelForm):
    istochnik = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control ml-0'}),
        label='Назовите источник получения информации о данной здравнице',
        required=False # Make this field optional
    )
    age = forms.IntegerField(label="Возраст", required=False)
    gender = forms.ChoiceField(
        choices=(('м', 'М'), ('ж', 'Ж'), ('', '')),
        # widget=forms.RadioSelect,
        label="Пол",
        required = False

    )
    city = forms.CharField(label="Город", required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),label='Ваши пожелания', required=False)

    class Meta:
        model = Review
        fields = ['goal_choice',
                  'visit_choice',
                  'istochnik',
                  'kak_preobletali',
                  'gruppa',
                  'treatment_rating',
                  'service_rating',
                  'projivanie',
                  'pitanie',
                  'soc_deatel',
                  'kval_med_pers',
                  'vrach',
                  'sred_med',
                  'obsluj',
                  'kak_v_celom',
                  'kakova_ver',
                  'age',
                  'gender',
                  'city',
                  'text',]
        labels = {
            'goal_choice': 'Цель выбора здравницы',
            'visit_choice': 'Посещаете данную здравницу',
            'istochnik': 'Назовите источник получения информации о данной здравнице',
            'kak_preobletali': 'Как приоблетали путевку',
            'gruppa': 'Имеете ли Вы установленную группу ограничения трудоспособности',
            'treatment_rating': 'Оцените качество лечения',
            'service_rating': 'Оцените качество сервисых услуг',
            'projivanie': 'Оцените качество проживание',
            'pitanie': 'Оцените качество питание',
            'soc_deatel': 'Оцените качество социокультурной деятельности',
            'kval_med_pers': 'Оцените качество квалификации медицинского персонала',
            'vrach': 'Оценка культуры обслуживания врачей',
            'sred_med': 'Оценка культуры обслуживания среднего медицинского персонала',
            'obsluj': 'Оценка культуры обсуживающего персонала',
            'kak_v_celom': 'Как в целом Вы можете оценить впечатления от пребывания в санатории',
            'kakova_ver': 'Какова вероятность что вы порекомендуете данную здравницу друзьям',
            'age': 'Возраст',
            'gender': 'Пол',
            'city': 'Город',
            'text': '',
        }

    def save(self, commit=True, user=None):
        review = super().save(commit=False)
        review.user = user
        if commit:
            review.save()
        return review


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['goal_choice', 'comment']