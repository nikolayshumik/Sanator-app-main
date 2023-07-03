from django.urls import path
from . import views
from .views import register_view
from .views import review_view
from .views import login_view
from .views import my_logout_view
from .views import расписаниедневное
from .views import feedbacks
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', views.base, name='home'),
    path('ban', views.ban, name='ban'),
    path('rules', views.rules, name='rules'),
    path('daily', views.daily, name='daily'),
    path('posters', views.posters, name='posters'),
    path('link', views.link, name='link'),
    path('map', views.map, name='map'),
    path('services', views.services, name='services'),
    path('daily/', расписаниедневное, name='daily-view'),
    path('schedule/<int:user_id>/<str:day>/', views.расписаниепользователя, name='schedule-for-user'),
    path('login/', login_view, name='login'),
    path('logout/', my_logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('review/', views.review_view, name='review'),
    path('feedbacks/', feedbacks, name='feedbacks'),
    path('sw.js', views.ServiceWorkerView.as_view(), name=views.ServiceWorkerView.name,),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)