# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from parser_a11social_json import fill_topic_models, parse_to_model
from vkontakte_groups.models import Group
from vkontakte_ads.models import Account, Campaign, Ad, TargetingStats
from vkontakte_mediaplanning.models import GroupAdditionalData, GroupTopicSet, GroupTopic

from vkontakte_mediaplanning.views import groups

''' TODO: Uncomment
class TestTopicParser(TestCase):

    def test_topic_parser(self):
        self.assertEqual(GroupTopic.objects.count(), 0)
        self.assertEqual(GroupTopicSet.objects.count(), 0)
        fill_topic_models()
        self.assertNotEqual(GroupTopic.objects.count(), 0)
        self.assertNotEqual(GroupTopicSet.objects.count(), 0)
        self.assertEqual(GroupTopic.objects.filter(grouptopicset=None).count(), 3)

    def test_allsocial_parser(self):
        self.assertEqual(GroupAdditionalData.objects.count(), 0)
        parse_to_model()
        self.assertEqual(GroupAdditionalData.objects.count(), 100)
        for i in GroupAdditionalData.objects.all():
            if i.grouptopics.count() == 0: print i.pk
            self.assertNotEqual(i.grouptopics.count(), 0)


class TestVkAdsAPIWithParameters(TestCase):
    #TODO переписать тест для реальных значений

    def test_targeting_stats(self):
        #prepare to work with ad account
        Account.remote.fetch()
        account = Account.objects.get()

        #TODO get gids from user selection in web table
        gids = {'1':None, '3':None}

        #get user selected parameters
        filters = {'sex':1, 'age_from':20, 'age_to':30}

        for gid, v in gids:
            # get_user_count_for_gid(gid)
            stat = TargetingStats.remote.get(ad=Ad(account=account,
                                               layout__link_domain='www.ford.com',
                                               layout__link_url='http://www.ford.com/trucks/ranger/',
                                               targeting__groups=gid,
                                               targeting__age_from=filters['age_from'],
                                               targeting__age_to=filters['age_to'],
                                               targeting__sex=filters['sex']))
            gids[gid] = stat.audience_count

        print gids

'''

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/seeding/')
        self.assertEqual(found.func, groups)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = groups(request)
        expected_html = render_to_string('home_page.html')
        self.assertEqual(response.content.decode(), expected_html)

