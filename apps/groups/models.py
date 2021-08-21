from django.db import models
from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Group(models.Model):
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

