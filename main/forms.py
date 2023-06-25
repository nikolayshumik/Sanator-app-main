from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review
from .models import UserProfile
from django.contrib.auth import get_user_model
from main.models import UserProfile
from django.forms import ModelForm
from .models import Posters
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
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))

    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': ''}

    def save(self, commit=True, user=None, phone_number=None):
        review = super().save(commit=False)
        review.user = user
        review.phone_number = phone_number
        if commit:
            review.save()
        return review


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)