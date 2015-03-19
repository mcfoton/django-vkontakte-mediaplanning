# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_groups.models import Group


class GroupTopicSet(models.Model):
    name = models.CharField(u'Группа тем', max_length=20, help_text='Группа тем, например "Спорт", "Мода и стиль". Заполняется парсингом и в будущем дерево топиков будет пересмотрено.')

    def __unicode__(self):
        #TODO разобраться почему консоль вместо красоты выдает <GroupTopicSet: [Bad Unicode data]>
        return str(self.id).encode('utf-8') + str(self.name).encode('utf-8')


class GroupTopic(models.Model):
    name = models.CharField(u'Тема', max_length=20, help_text='Тема внутри группы тем. Например, "Футбол" и "Баскетбол" внутри группы тем "Спорт". Заполняется парсингом и в будущем дерево топиков будет пересмотрено.')
    grouptopicset = models.ForeignKey(GroupTopicSet, null=True, help_text='Могут быть темы которые не принадлежат какому-то набору, сами по себе.')

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.name)


#model for additional data from allsocial
class GroupAdditionalData(models.Model):

    vk_id = models.OneToOneField(Group, primary_key=True)
    date = models.DateTimeField(u'Дата парсинга')

    grouptopics = models.ManyToManyField(GroupTopic, verbose_name='Тема')

    in_search = models.BooleanField(u'В поиске', help_text='Находится ли это сообщество в поиске ВК по сообществам')
    cpp = models.IntegerField(u'Стоимость размещения поста', help_text='Стоимость размещения одного поста в сообществе. Заполняется парсингом и по ходу работы обновляется пользователем вручную.')

    audience_count = models.IntegerField(u'Аудитория c учетом фильтра', null=True, help_text='Число пользователей с учетом фильтров. Значение получается после запроса к рекламному кабинету с vk_id и других метрик в качестве фильтра.')

    def __unicode__(self):
        return str(self.vk_id)




#parse allsocial to a model with parser_a11social_json.py
#daily update basic data for groups from VK

#update table with new user count

#Interface
    #show table with basic data
    #get parameters
    #show updated table
