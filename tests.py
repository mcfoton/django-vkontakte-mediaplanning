from django.test import TestCase
# from parser_a11sosial_json import parse_to_model
from vkontakte_ads.models import Account, Campaign, Ad, TargetingStats

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


'''
class TestGroupBasicData(TestCase):
    def test_basic_data(self):
        """
        Tests if basic data is collected properly
        """

        self.assertEqual(GroupData.objects.count(), 0)

        GroupData.remote.fetch(ids=[1, 3])
        self.assertNotEqual(GroupData.objects.count(), 0)
        self.assertEqual(GroupData.objects.get(pk=1).screen_name, 'apiclub')
        self.assertGreater(GroupData.objects.get(pk=1).members_count, 0)
        self.assertEqual(GroupData.objects.get(pk=3).screen_name, 'club3')
        self.assertGreater(GroupData.objects.get(pk=3).members_count, 0)


class TestAllSocialParsed(TestCase):
    def test_parsing_to_db(self):
        parse_to_model()
'''
