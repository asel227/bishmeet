from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.groups.models import Category, Group, Rating


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=Category.objects.all(),
    )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'category_id',
                  'category', 'interests', 'pictures')


class GroupDetailSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id', 'name', 'description', 'category_id',
            'category', 'pictures', 'file'
        )


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
