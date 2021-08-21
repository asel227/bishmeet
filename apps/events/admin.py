from django.contrib import admin

from apps.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['group', 'name', 'location', 'description', 'event_date',
                    'event_time', 'timestamp', 'pictures', 'active']


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['text', 'event', 'user', 'create_at']