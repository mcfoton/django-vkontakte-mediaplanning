from django.test import TestCase
from vkontakte_mediaplanning.models import GroupData

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

