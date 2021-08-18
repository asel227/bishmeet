from django.contrib import admin

from apps.groups.models import Group, Category, Rating


@admin.register(Category)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'interests', 'pictures']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['start', 'group', 'user']
