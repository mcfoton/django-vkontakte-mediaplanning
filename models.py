# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_api.models import VkontaktePKModel
from vkontakte_groups.models import Group, GroupRemoteManager

GROUP_TYPE_CHOICES = (
    ('group',  u'Группа'),
    ('page',  u'Страница'),
    ('event',  u'Событие'),
)

#daily get basic data about groups
class GroupDataRemoteManager(GroupRemoteManager):
    pass

class GroupData(VkontaktePKModel):
    class Meta:
        verbose_name = 'Vkontakte group basic data'
        verbose_name_plural = 'Vkontakte group basic data'

    resolve_screen_name_types = ['group','page','event']
    methods_namespace = 'groups'
    remote_pk_field = 'gid'
    slug_prefix = 'club'

    name = models.CharField(max_length=800)
    screen_name = models.CharField(u'Короткое имя группы', max_length=50, db_index=True)
    is_closed = models.NullBooleanField(u'Флаг закрытой группы')
    is_admin = models.NullBooleanField(u'Пользователь является администратором')
    members_count = models.IntegerField(u'Всего участников', null=True)
    type = models.CharField(u'Тип объекта', max_length=10, choices=GROUP_TYPE_CHOICES)

    photo = models.URLField()
    photo_big = models.URLField()
    photo_medium = models.URLField()

    remote = GroupDataRemoteManager(remote_pk=('remote_id',), methods={
        'get': 'getById',
        'search': 'search',
    })

    def __unicode__(self):
        return self.name

    def remote_link(self):
        return 'http://vk.com/club%d' % self.remote_id

    @property
    def refresh_kwargs(self):
        return {'ids': [self.remote_id]}

    def fetch_statistic(self, *args, **kwargs):
        if 'vkontakte_groups_statistic' not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured("Application 'vkontakte_groups_statistic' not in INSTALLED_APPS")

        from vkontakte_groups_statistic.models import fetch_statistic_for_group
        return fetch_statistic_for_group(group=self, *args, **kwargs)

#show table with basic data
#get additional filters

#create placeholder ad

#for each group id from above
    #pass each group id as parameter
    #pass all additional filters for that group
    #get user count

#update table with new user count