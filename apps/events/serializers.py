from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.events.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'group', 'name', 'location', 'description',
                  'event_date', 'event_time', 'pictures')


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'group', 'name', 'location', 'description',
            'event_date', 'event_time', 'pictures', 'active'
        )

#
# class CommentSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

