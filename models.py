# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_api.models import VkontaktePKModel
from vkontakte_groups.models import Group
from vkontakte_groups_statistic.models import GroupStatistic
from vkontakte_ads.models import Account, Ad, TargetingStats

#model with additional fields
class GroupAdditionalData(models.Model):

    vk_id = models.ForeignKey(Group)

    cat_id_priv = models.CharField(max_length=100)
    cat_id_pub = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    in_search = models.IntegerField(u'В поиске')
    cpp = models.IntegerField()

    def __str__(self):
        return str(self.vk_id)

class GroupAdsFilter(VkontaktePKModel):
    group = models.OneToOneField(Group)
    audience_count = models.IntegerField(u'Аудитория', null=True)

#parse allsocial to a model with parser_a11social_json.py
#daily update basic data for groups from VK

        

#update table with new user count

#Interface
    #show table with basic data
    #get parameters
    #show updated table