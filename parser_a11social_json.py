import json, requests

#connecting to django model
import os
import sys
sys.path.append('/Users/mcfoton/Documents/dev/learning/envs/dev/gravitytool/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gravitytool.settings'
from vkontakte_mediaplanning.models import AllSocialParsed

def parse_to_model():

    total_count = json.loads(requests.get('http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=204924&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1').text)['response']['total_count']
    total_pages = total_count / 25 + 1 #number of requests. one response carries 25 entries

    for page in range(total_pages):
        print '%s groups in db' % AllSocialParsed.objects.count()

        offset = page*25
        url = 'http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=' + str(offset) + '&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1'
        # url = 'http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=0&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1' #url for testing with offset=0

        response = requests.get(url)
        json_data = json.loads(response.text)

        for i in range(25):
            group = json_data['response']['entity'][i]
            group['gid'] = group.pop('id')
            _cat = group.pop('category')
            group['cat_id_priv'] = ','.join(_cat['private'])
            group['cat_id_pub'] = ','.join(_cat['public'])
            AllSocialParsed.objects.create(**group)


parse_to_model()