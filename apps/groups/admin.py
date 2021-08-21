from django.contrib import admin

from apps.groups.models import Group, Category


@admin.register(Category)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'interests', 'pictures']
