# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_groups.models import Group

#model for Topic Sets. i.e. 'Sports'
class GroupTopicSet(models.Model):
    topicset = models.CharField(u'Группа тем', max_length=20)

    def __unicode__(self):
        return str(self.topicset)

#model for Topics inside Topic Set. i.e. 'Football', 'Baseball'
class GroupTopic(models.Model):
    topic = models.CharField(u'Тема', max_length=20)
    grouptopicset = models.ForeignKey(GroupTopicSet)

    def __unicode__(self):
        return str(self.t)


#model for additional data from allsocial
class GroupAdditionalData(models.Model):

    vk_id = models.OneToOneField(Group, primary_key=True)
    date = models.DateTimeField(u'Дата парсинга')
    
    grouptopics = models.ManyToManyField(GroupTopic, verbose_name='Тема')
    grouptopicsets = models.ManyToManyField(GroupTopicSet, verbose_name='Группа тем')
    
    in_search = models.BooleanField(u'В поиске')
    cpp = models.IntegerField(u'Стоимость размещения поста')

    #this field is updated only when group id is sent to ads API
    audience_count = models.IntegerField(u'Аудитория c учетом фильтра')

    def __unicode__(self):
        return str(self.vk_id)




#parse allsocial to a model with parser_a11social_json.py
#daily update basic data for groups from VK

#update table with new user count

#Interface
    #show table with basic data
    #get parameters
    #show updated table