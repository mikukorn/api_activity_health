from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'height', 'weight', 'bmi',)
    empty_value_display = '-пусто-'


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'value', 'created_at',)
    empty_value_display = '-пусто-'


class DaySummaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total_food', 'total_calories', 'total_summary',)
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(DaySummary, DaySummaryAdmin)
