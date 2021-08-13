from django.db import models

from apps.users.models import User
from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Group(models.Model):
    objects = None
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='group',
                                 null=True)
    interests = models.CharField(verbose_name='Интересы', max_length=255)
    pictures = models.ImageField(upload_to=upload_instance, null=True, verbose_name="Картинки")

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Rating(models.Model):
    start = models.SmallIntegerField(verbose_name='Количество звезд')
    group = models.ForeignKey(to=Group,
                              on_delete=models.CASCADE,
                              related_name='group_ratings')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name='user_ratings',
                             null=True)

    class Meta:
        verbose_name = 'Статистика группы'
        verbose_name_plural = 'Статистики групп'

    def __str__(self):
        return f'Группа: {self.group.name}, статистика: {self.start}'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    group = models.ForeignKey(to=Group,
                              on_delete=models.CASCADE,
                              related_name='group_comments')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name='user_comments',
                             null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text[:100]}...'
