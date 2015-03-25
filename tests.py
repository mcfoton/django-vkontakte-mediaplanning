# -*- coding: utf-8 -*-

from django.test import TestCase
from parser_a11social_json import fill_topic_models, parse_to_model
from vkontakte_groups.models import Group
# from vkontakte_ads.models import Account, Campaign, Ad, TargetingStats
from vkontakte_mediaplanning.models import GroupAdditionalData, GroupTopicSet, GroupTopic

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

    def test_targeting_stats(self):

        stat = TargetingStats.remote.get(ad=Ad(account=AccountFactory(remote_id=ACCOUNT_ID),
                                               layout__link_domain='www.ford.com',
                                               layout__link_url='http://www.ford.com/trucks/ranger/',
                                               targeting__sex=2,
                                               targeting__age_from=20,
                                               targeting__age_to=30))

        self.assertTrue(stat.audience_count > 0)
        self.assertTrue(stat.recommended_cpc > 0)
        self.assertTrue(stat.recommended_cpm > 0)


from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from vkontakte_mediaplanning.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home_page.html')
        self.assertEqual(response.content.decode(), expected_html)
'''
    def test_ads_api_is_working(self):
        Account.remote.fetch()
        account = Account.objects.get(pk=1600459782)
        account.fetch_campaigns()
        campaign = Campaign.objects.get(pk=1000586044)



class TestUserCounts(TestCase):
    def test_user_counts(self):
        ids = [28764987]
        self.assertEqual(Account.objects.count(), 0)
        self.assertEqual(Targeting.objects.count(), 0)
        self.assertEqual(Ad.objects.count(), 0)
        #TODO make smart selection from actual campaings and ads of the user
        Account.remote.fetch()
        account = Account.objects.get()
        account.fetch_campaigns()
        campaign = account.campaigns.get()
        campaign.fetch_ads()
        campaign.fetch_ads_targeting()
        self.assertEqual(Targeting.objects.count(), 1)
        self.assertEqual(Targeting.objects.get().count, 641)

    def get_user_counts(self):
        #prepare to work with ad account
        Account.remote.fetch()
        account = Account.objects.get()

        gids = {'1':None, '3':None} #TODO get gids from user selection in web table
        filters = {'sex':1, 'age_from':20, 'age_to':30} #get user selected parameters

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


class TestAllSocialParsed(TestCase):
    def test_parsing_to_db(self):
        parse_to_model()
'''
