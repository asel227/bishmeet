from django.db import models

from apps.events.models import Event
from apps.groups.models import Group
from apps.users.models import User

city_choices = (
    ('1', 'Бишкек'),
    ('2', 'Ыссык-Кол'),
    ('3', 'Жалал-Абад'),
    ('4', 'Ош'),
    ('5', 'Баткен'),
    ('6', 'Талас'),
    ('7', 'Нарын'),
)


class MyProfile(models.Model):
    profile = models.ForeignKey(to=User,
                                on_delete=models.SET_NULL,
                                related_name='users_profile',
                                null=True)
    location = models.CharField(verbose_name='Локация', max_length=20, choices=city_choices, default=True)
    my_group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                                 related_name='group', verbose_name='Мои группы', null=True)
    my_event = models.ForeignKey(Event, on_delete=models.SET_NULL,
                                 related_name='events', verbose_name='Мои мероприятия', null=True)
