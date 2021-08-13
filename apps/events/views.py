import json

from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.events.models import Event
from apps.events.serializers import EventDetailSerializer, EventSerializer, CommentSerializer
from apps.events.models import Group, Comment


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        event = context.get('event')
        context['first_picture'] = event.get_first_picture
        context['comments'] = Comment.objects.filter(
            event__id=event.id
        ).order_by('-create_at')[:4]

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())

        event = Event.objects.filter(id=data.get('event_id')).first()

        if event is None:
            return JsonResponse({'detail': 'error'}, status=404)

        Comment.objects.create(
            user=request.user,
            product=event,
            text=data.get('comment'),
        )

        return JsonResponse({'detail': 'success'}, status=201)


class EventCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        queryset = super(EventCreateAPIView, self).filter_queryset(queryset)
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name_icontains=name)

        return queryset


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventDetailSerializer


@api_view(['GET'])
def comments_list(request):
    comments = Comment.objects.all()

    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(instance=comment)
        return Response(serializer.data)
