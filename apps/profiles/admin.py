from django.contrib import admin

from apps.profiles.models import MyProfile


@admin.register(MyProfile)
class MyProfileAdmin(admin.ModelAdmin):
    list_display = ['profile', 'location', 'my_group', 'my_event']
