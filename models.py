# -*- coding: utf-8 -*-
from django.db import models
from vkontakte_api.models import VkontaktePKModel
from vkontakte_groups.models import Group

class AllSocialParsed(models.Model):

	diff_abs = models.IntegerField(u'Прирост в числах')
	cat_id_priv = models.CharField(max_length=100)
	cat_id_pub = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	diff_rel = models.FloatField(u'Прирост в процентах')
	visitors = models.IntegerField(u'Посетители')
	type_id = models.IntegerField()
	reach = models.IntegerField(u'Охват')
	in_search = models.IntegerField(u'В поиске')
	vk_id = models.IntegerField()
	caption = models.CharField(max_length=100)
	can_change_cpp = models.IntegerField()
	avatar = models.CharField(max_length=100)
	cpp = models.IntegerField()
	gid = models.IntegerField(primary_key=True)
	is_verified = models.IntegerField()
	is_closed = models.IntegerField()
	quantity = models.IntegerField()

	def __str__(self):
		return str(self.vk_id)

#parse allsocial to a model with parser_a11social_json.py
#daily update basic data for groups from VK

#get additional filters
class GroupAdsFilter(VkontaktePKModel):
    group = models.OneToOneField(Group)
    filtered_user_count = models.IntegerField(u'Аудитория', null=True)


#create placeholder ad

#for each group id from above
    #pass each group id as parameter
    #pass all additional filters for that group
    #get user count

#update table with new user count

#Interface
	#show table with basic data
	#get parameters
	#show updated table