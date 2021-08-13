import json

from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.groups.models import Group, Comment
from apps.groups.serializers import GroupSerializer, GroupDetailSerializer, CommentSerializer


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        group = context.get('group')
        context['first_picture'] = group.get_first_picture
        context['comments'] = Comment.objects.filter(
            group__id=group.id
        ).order_by('-create_at')[:3]

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())

        group = Group.objects.filter(id=data.get('group_id')).first()

        if group is None:
            return JsonResponse({'detail': 'error'}, status=404)

        Comment.objects.create(
            user=request.user,
            product=group,
            text=data.get('comment'),
        )

        return JsonResponse({'detail': 'success'}, status=201)

# class AsyncProductListView(ListView):
#     queryset = Product.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body.decode())
#         products_list = self.queryset.filter(name__icontains=data.get('value'))
#         context = {'products_list': products_list}
#         html = render_to_string(template_name='partials/product_list.html',
#                                 context=context,
#                                 request=request)
#
#         return JsonResponse({'html': html}, status=200)


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def filter_queryset(self, queryset):
        queryset = super(GroupListCreateAPIView, self).filter_queryset(queryset)
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name_icontains=name)

        return queryset


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GroupDetailSerializer


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