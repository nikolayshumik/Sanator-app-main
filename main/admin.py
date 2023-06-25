from django.contrib import admin
from .models import Rools
from .models import Posters
from .models import Zapret
from .models import Rasporiadok
from .models import Review
from .models import UserProfile
from .models import UserDailySchedule

from django.contrib.auth.admin import UserAdmin



@admin.register(UserDailySchedule)
class UserDailyScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'weekday', 'schedule')
    list_filter = ('user', 'weekday',)
    search_fields = ['user__username']


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'last_name', 'phone_number', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('last_name', 'phone_number', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'last_name', 'phone_number', 'password1', 'password2'),
        }),
    )






admin.site.register(Rools)
admin.site.register(Posters)
admin.site.register(Zapret)
admin.site.register(Rasporiadok)
admin.site.register(Review)
admin.site.register(UserProfile)



