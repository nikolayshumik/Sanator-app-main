from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Rools
from .models import Posters
from .models import Zapret
from .models import Rasporiadok
from .forms import ImageForm
from .models import Scheduledaily
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from main.forms import CustomUserCreationForm
from .models import UserDailySchedule
from datetime import datetime



def base(request):
    return render(request, 'main/base.html')

def rules(request):
    rools = Rools.objects.all()
    return render(request, 'main/rules.html', {'rools': rools})


def daily(request):
    rasporiadok = Rasporiadok.objects.all()
    return render(request, 'main/daily.html', {'rasporiadok': rasporiadok})

def posters(request):
    posters = Posters.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'main/posters.html', {'posters': posters, 'form': form})


def dayz(request):
    return render(request, 'main/dayZ.html')

def link(request):
    # zapret = Zapret.objects.all()
    return render(request, 'main/link.html')
    # {'zapret': zapret})

def ban(request):
    zapret = Zapret.objects.all()
    return render(request, 'main/ban.html', {'zapret': zapret})

def map(request):
    return render(request, 'main/map.html')
# рабочая админ панель
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def review_view(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
            else:
                # Обработка ошибки, например, перенаправление на страницу входа
                return redirect('login')
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'main/review.html', {'reviews': reviews, 'form': form})

@login_required
def schedule(request):
    user_schedule = Scheduledaily.objects.filter(user=request.user)
    context = {'user_schedule': user_schedule}
    return render(request, 'main/schedule-view.html', context)

def authenticate_by_phone_number(request, phone_number):
    try:
        user_profile = UserProfile.objects.get(phone_number=phone_number)
        user = user_profile.user
    except UserProfile.DoesNotExist:
        return None
    return user


def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')

my_logout_view = MyLogoutView.as_view()


@login_required
def daily_view(request):
    user = request.user
    weekday_schedules = {}
    for schedule in UserDailySchedule.objects.filter(user=user):
        weekday_schedules.setdefault(schedule.weekday, []).append(schedule)
    context = {'weekday_schedules': weekday_schedules}
    return render(request, 'main/schedule-view.html', context)

def schedule_for_user(request, user_id, day):
    # Получаем расписание для выбранного пользователя на выбранный день
    schedules = UserDailySchedule.objects.filter(user_id=user_id, weekday=day).order_by('start_time')

    context = {'schedules': schedules}

    return render(request, 'main/schedule-view.html', context)

class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'


