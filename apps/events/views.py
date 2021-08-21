import json

import django_filters
from django.db import models as django_models
from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import status, filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.events.models import Event
from apps.events.serializers import EventDetailSerializer, EventSerializer


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        event = context.get('event')
        context['first_picture'] = event.get_first_picture
        # context['comments'] = Comment.objects.filter(
        #     event__id=event.id
        # ).order_by('-create_at')[:4]

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())

        event = Event.objects.filter(id=data.get('event_id')).first()

        if event is None:
            return JsonResponse({'detail': 'error'}, status=404)

        # Comment.objects.create(
        #     user=request.user,
        #     product=event,
        #     text=data.get('comment'),
        # )

        return JsonResponse({'detail': 'success'}, status=201)


class EventFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(name="timestamp", lookup_expr='gte')

    class Meta:
        model = Event
        fields = ['event_date', 'event_time', 'timestamp', 'timestamp_gte']


class EventListViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_class = EventFilter
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['=name', '=group']


class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        queryset = super(EventListCreateAPIView, self).filter_queryset(queryset)
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name_icontains=name)

        return queryset


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventDetailSerializer


# @api_view(['GET'])
# def comments_list(request):
#     comments = Comment.objects.all()
#
#     serializer = CommentSerializer(comments, many=True)
#
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail(request, pk):
#     try:
#         comment = Comment.objects.get(pk=pk)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CommentSerializer(instance=comment)
#         return Response(serializer.data)
