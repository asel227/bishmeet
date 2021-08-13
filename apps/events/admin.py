from django.contrib import admin

from apps.events.models import Event, Rating, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['group', 'name', 'location', 'description', 'event_date', 'event_time', 'pictures', 'active']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['start', 'event', 'user']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'event', 'user']