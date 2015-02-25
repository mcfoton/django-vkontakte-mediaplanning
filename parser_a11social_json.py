import json, requests

#connecting to django model
import os
import sys
sys.path.append('/Users/mcfoton/Documents/dev/learning/envs/dev/gravitytool/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gravitytool.settings'
from vkontakte_groups.models import Group
from vkontakte_groups_statistic.models import GroupStatistic
from vkontakte_mediaplanning.models import GroupAdditionalData

def parse_to_model():

    total_count = json.loads(requests.get('http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=204924&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1').text)['response']['total_count']
    total_pages = total_count / 25 + 1 #number of requests. one response carries 25 entries

    for page in range(total_pages):
        print '%s groups in db' % GroupAdditionalData.objects.count()

        offset = page*25
        url = 'http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=' + str(offset) + '&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1'
        # response = requests.get(http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=0&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1')

        response = requests.get(url)
        json_data = json.loads(response.text)

        for i in range(25):
            group = json_data['response']['entity'][i]

            #removing excess data
            group.pop('diff_abs')
            group.pop('diff_rel')
            group.pop('can_change_cpp')
            group.pop('diff_rel')
            group.pop('avatar')
            group.pop('id')


            #renaming response fields to match Group model
            group['remote_id'] = group.pop('vk_id')
            group['members_count'] = group.pop('quantity')
            group['photo_200'] = group.pop('avatar')
            group['type'] = group.pop('type_id')
            group['name'] = group.pop('caption')


            #statistics
            reach = group.pop('reach')
            visitors = group.pop('visitors')
            in_search = group.pop('in_search')
            cpp = group.pop('cpp')
            statistics = {}
            statistics['reach'] = reach
            statistics['visitors'] = visitors
            GroupStatistic.objects.create(**statistics)


            _cat = group.pop('category')
            group['cat_id_priv'] = ','.join(_cat['private'])
            group['cat_id_pub'] = ','.join(_cat['public'])
            GroupAdditionalData.objects.create(**group)
            group.pop('cat_id_priv')
            group.pop('cat_id_pub')



            #sending the rest to Group model
            Group.objects.create(**group)


parse_to_model()