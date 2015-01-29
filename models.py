# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_api.models import VkontaktePKModel
from vkontakte_groups.models import Group, GroupRemoteManager

#daily update basic data for groups
class GroupDataRemoteManager(GroupRemoteManager):
    pass

class GroupAdsFilter(VkontaktePKModel):
    group = models.OneToOneField(Group, primary_key=True)
    filtered_user_count = models.IntegerField(u'Аудитория', null=True)
    

#show table with basic data
#get additional filters

#create placeholder ad

#for each group id from above
    #pass each group id as parameter
    #pass all additional filters for that group
    #get user count

#update table with new user count