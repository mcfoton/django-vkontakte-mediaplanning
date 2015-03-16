# -*- coding: utf-8 -*-

import json, requests
from datetime import datetime
from vkontakte_groups.models import Group
from vkontakte_groups_statistic.models import GroupStatistic
from vkontakte_mediaplanning.models import GroupAdditionalData, GroupTopicSet, GroupTopic

def parse_categories():
    """
    This method was used to parse categories. Resulting topicsets dictionary
    is assigned directly in parse_to_model() method.
    json_data = {u'error_status': -1, u'error_message': u'', u'response': {u'public': {u'-1': {u'category': {u'1': {u'is_parent': -1, u'parent_id': -1, u'is_active': 1, u'id': 60, u'caption': u'\u042e\u043c\u043e\u0440', u'order': 3, u'slug': u'yumor'}, u'0': {u'is_parent': -1, u'parent_id': -1, u'is_active': 1, u'id': 52, u'caption': u'\u041c\u043e\u043b\u043e\u0434\u0451\u0436\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 32, u'slug': u'teens'}, u'2': {u'is_parent': -1, u'parent_id': -1, u'is_active': 1, u'id': 4, u'caption': u'\u041c\u043e\u0434\u0430', u'order': 2, u'slug': u'fashion'}}, u'group': {u'order': -1}}, u'69': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 70, u'caption': u'\u0424\u0438\u0442\u043d\u0435\u0441', u'order': 21, u'slug': u'Fitness'}, u'0': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 74, u'caption': u'\u0421\u043f\u043e\u0440\u0442 (\u0434\u0440\u0443\u0433\u043e\u0435)', u'order': 22, u'slug': u'sportother'}, u'3': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 36, u'caption': u'\u0424\u0443\u0442\u0431\u043e\u043b', u'order': 21, u'slug': u'football'}, u'2': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 71, u'caption': u'\u0421\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u043e\u0435 \u043f\u0438\u0442\u0430\u043d\u0438\u0435', u'order': 21, u'slug': u'sportdiet'}, u'5': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 73, u'caption': u'\u041f\u043e\u0445\u0443\u0434\u0435\u043d\u0438\u0435', u'order': 22, u'slug': u'diet'}, u'4': {u'is_parent': -1, u'parent_id': 69, u'is_active': 1, u'id': 72, u'caption': u'Workout', u'order': 22, u'slug': u'Workout'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 69, u'caption': u'\u0421\u043f\u043e\u0440\u0442 \u0438 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435', u'order': 7, u'slug': u'sporthealth'}}, u'77': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 77, u'is_active': 1, u'id': 79, u'caption': u'\u0421\u0442\u0430\u0440\u0442\u0430\u043f\u044b', u'order': 16, u'slug': u'Startups'}, u'0': {u'is_parent': -1, u'parent_id': 77, u'is_active': 1, u'id': 26, u'caption': u'\u041c\u043e\u0442\u0438\u0432\u0430\u0446\u0438\u044f', u'order': 16, u'slug': u'motivation'}, u'2': {u'is_parent': -1, u'parent_id': 77, u'is_active': 1, u'id': 78, u'caption': u'\u0424\u0438\u043d\u0430\u043d\u0441\u044b', u'order': 16, u'slug': u'Finance'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 77, u'caption': u'\u0411\u0438\u0437\u043d\u0435\u0441', u'order': 10, u'slug': u'Biz'}}, u'80': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 80, u'is_active': 1, u'id': 47, u'caption': u'\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438', u'order': 16, u'slug': u'suggested'}, u'0': {u'is_parent': -1, u'parent_id': 80, u'is_active': 1, u'id': 81, u'caption': u'\u0417\u043d\u0430\u043a\u043e\u043c\u0441\u0442\u0432\u0430', u'order': 16, u'slug': u'meetings'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 80, u'caption': u'\u0417\u043d\u0430\u043a\u043e\u043c\u0441\u0442\u0432\u0430 \u0438 \u043e\u0431\u0449\u0435\u043d\u0438\u0435', u'order': 10, u'slug': u'friends'}}, u'63': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 63, u'is_active': 1, u'id': 9, u'caption': u'\u042d\u0440\u043e\u0442\u0438\u043a\u0430/\u041f\u043e\u0440\u043d\u043e', u'order': 22, u'slug': u'erotica'}, u'0': {u'is_parent': -1, u'parent_id': 63, u'is_active': 1, u'id': 39, u'caption': u'\u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0435 \u0434\u0435\u0432\u0443\u0448\u043a\u0438', u'order': 22, u'slug': u'beautiful'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 63, u'caption': u'\u0414\u0435\u0432\u0443\u0448\u043a\u0438', u'order': 8, u'slug': u'girls'}}, u'82': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 82, u'is_active': 1, u'id': 46, u'caption': u'\u0421\u0432\u0430\u0434\u0435\u0431\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 16, u'slug': u'wedding'}, u'0': {u'is_parent': -1, u'parent_id': 82, u'is_active': 1, u'id': 40, u'caption': u'\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f', u'order': 16, u'slug': u'relations'}, u'3': {u'is_parent': -1, u'parent_id': 82, u'is_active': 1, u'id': 83, u'caption': u'\u0414\u0435\u0442\u0438', u'order': 16, u'slug': u'kids'}, u'2': {u'is_parent': -1, u'parent_id': 82, u'is_active': 1, u'id': 84, u'caption': u'\u041e\u0431\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u0438 \u0440\u0435\u043c\u043e\u043d\u0442', u'order': 15, u'slug': u'settlement'}, u'4': {u'is_parent': -1, u'parent_id': 82, u'is_active': 1, u'id': 38, u'caption': u'\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 10, u'slug': u'parents'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 82, u'caption': u'\u0421\u0435\u043c\u044c\u044f \u0438 \u0434\u043e\u043c', u'order': 10, u'slug': u'family'}}, u'108': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 108, u'is_active': 1, u'id': 32, u'caption': u'\u0420\u0435\u043a\u043b\u0430\u043c\u0430', u'order': 8, u'slug': u'advertising'}, u'0': {u'is_parent': -1, u'parent_id': 108, u'is_active': 1, u'id': 6, u'caption': u'\u0421\u041c\u0418', u'order': 5, u'slug': u'media'}, u'2': {u'is_parent': -1, u'parent_id': 108, u'is_active': 1, u'id': 33, u'caption': u'\u0417\u043d\u0430\u043c\u0435\u043d\u0438\u0442\u043e\u0441\u0442\u0438', u'order': 7, u'slug': u'celebrity'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 108, u'caption': u'\u0421\u041c\u0418, \u0440\u0435\u043a\u043b\u0430\u043c\u0430 \u0438 PR', u'order': 12, u'slug': u'advert'}}, u'99': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 99, u'is_active': 1, u'id': 56, u'caption': u'\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438', u'order': 5, u'slug': u'professional'}, u'0': {u'is_parent': -1, u'parent_id': 99, u'is_active': 1, u'id': 100, u'caption': u'\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0430', u'order': 9, u'slug': u'Politics'}, u'3': {u'is_parent': -1, u'parent_id': 99, u'is_active': 1, u'id': 101, u'caption': u'\u0413\u0435\u043e\u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0430, \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u043a\u0430', u'order': 10, u'slug': u'economy'}, u'2': {u'is_parent': -1, u'parent_id': 99, u'is_active': 1, u'id': 55, u'caption': u'\u0420\u0435\u043b\u0438\u0433\u0438\u044f', u'order': 10, u'slug': u'religion'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 99, u'caption': u'\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u043e', u'order': 10, u'slug': u'people'}}, u'61': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 49, u'caption': u'\u0422\u0435\u043b\u0435\u0432\u0438\u0434\u0435\u043d\u0438\u0435', u'order': 23, u'slug': u'tv'}, u'0': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 37, u'caption': u'\u0418\u0433\u0440\u044b', u'order': 24, u'slug': u'games'}, u'3': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 41, u'caption': u'\u041d\u043e\u0441\u0442\u0430\u043b\u044c\u0433\u0438\u044f', u'order': 23, u'slug': u'nostalgia'}, u'2': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 53, u'caption': u'\u0410\u043d\u0438\u043c\u0435/\u0425\u0435\u043d\u0442\u0430\u0439', u'order': 24, u'slug': u'anime'}, u'5': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 48, u'caption': u'\u0412\u0438\u0434\u0435\u043e', u'order': 23, u'slug': u'video'}, u'4': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 43, u'caption': u'\u0423\u0436\u0430\u0441\u044b', u'order': 23, u'slug': u'Horror'}, u'7': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 7, u'caption': u'\u041c\u0443\u0437\u044b\u043a\u0430', u'order': 23, u'slug': u'music'}, u'6': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 57, u'caption': u'\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b', u'order': 23, u'slug': u'mult'}, u'8': {u'is_parent': -1, u'parent_id': 61, u'is_active': 1, u'id': 5, u'caption': u'\u041a\u0438\u043d\u043e\u0444\u0438\u043b\u044c\u043c\u044b', u'order': 22, u'slug': u'movies'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 61, u'caption': u'\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f', u'order': 10, u'slug': u'entertainment'}}, u'75': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 75, u'is_active': 1, u'id': 45, u'caption': u'\u041f\u0440\u0438\u0440\u043e\u0434\u0430', u'order': 21, u'slug': u'nature'}, u'0': {u'is_parent': -1, u'parent_id': 75, u'is_active': 1, u'id': 17, u'caption': u'\u041f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u044f', u'order': 21, u'slug': u'travel'}, u'2': {u'is_parent': -1, u'parent_id': 75, u'is_active': 1, u'id': 76, u'caption': u'\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435', u'order': 21, u'slug': u'Animal'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 75, u'caption': u'\u041f\u0440\u0438\u0440\u043e\u0434\u0430 \u0438 \u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u044f', u'order': 7, u'slug': u'naturetravel'}}, u'109': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 109, u'is_active': 1, u'id': 50, u'caption': u'\u0420\u043e\u0441\u0441\u0438\u044f', u'order': 6, u'slug': u'russia'}, u'0': {u'is_parent': -1, u'parent_id': 109, u'is_active': 1, u'id': 110, u'caption': u'\u041a\u0430\u0432\u043a\u0430\u0437\u0441\u043a\u0438\u0435', u'order': 7, u'slug': u'Kavkaz'}, u'3': {u'is_parent': -1, u'parent_id': 109, u'is_active': 1, u'id': 27, u'caption': u'\u0420\u0435\u0433\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 4, u'slug': u'regions'}, u'2': {u'is_parent': -1, u'parent_id': 109, u'is_active': 1, u'id': 114, u'caption': u'\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d', u'order': 8, u'slug': u'Kazahstan'}, u'4': {u'is_parent': -1, u'parent_id': 109, u'is_active': 1, u'id': 59, u'caption': u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430', u'order': 5, u'slug': u'ukrainskie'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 109, u'caption': u'\u0420\u0435\u0433\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 12, u'slug': u'region'}}, u'89': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 90, u'caption': u'\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0430', u'order': 5, u'slug': u'Architecture'}, u'0': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 21, u'caption': u'\u0418\u043d\u0442\u0435\u0440\u044c\u0435\u0440', u'order': 16, u'slug': u'interior'}, u'3': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 19, u'caption': u'\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', u'order': 12, u'slug': u'photo'}, u'2': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 91, u'caption': u'\u041b\u0430\u043d\u0434\u0448\u0430\u0444\u0442\u043d\u044b\u0439 \u0434\u0438\u0437\u0430\u0439\u043d', u'order': 17, u'slug': u'Landscape'}, u'5': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 22, u'caption': u'\u0414\u0438\u0437\u0430\u0439\u043d', u'order': 7, u'slug': u'design'}, u'4': {u'is_parent': -1, u'parent_id': 89, u'is_active': 1, u'id': 16, u'caption': u'\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438', u'order': 17, u'slug': u'pictures'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 89, u'caption': u'\u0418\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e, \u0434\u0438\u0437\u0430\u0439\u043d', u'order': 10, u'slug': u'artdesign'}}, u'103': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 106, u'caption': u'\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435', u'order': 10, u'slug': u'healthcare'}, u'0': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 112, u'caption': u'\u0414\u0440\u0443\u0433\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', u'order': 12, u'slug': u'services'}, u'3': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 105, u'caption': u'\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', u'order': 9, u'slug': u'realestate'}, u'2': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 104, u'caption': u'\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', u'order': 7, u'slug': u'companies'}, u'5': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 24, u'caption': u'\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u044b', u'order': 5, u'slug': u'shops'}, u'4': {u'is_parent': -1, u'parent_id': 103, u'is_active': 1, u'id': 107, u'caption': u'\u0422\u0443\u0440\u0438\u0437\u043c', u'order': 10, u'slug': u'Tourism'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 103, u'caption': u'\u0422\u043e\u0432\u0430\u0440\u044b \u0438 \u0443\u0441\u043b\u0443\u0433\u0438', u'order': 10, u'slug': u'goods'}}, u'68': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 68, u'is_active': 1, u'id': 15, u'caption': u'\u0414\u0438\u0435\u0442\u044b', u'order': 18, u'slug': u'diets'}, u'0': {u'is_parent': -1, u'parent_id': 68, u'is_active': 1, u'id': 13, u'caption': u'\u041a\u0440\u0430\u0441\u043e\u0442\u0430', u'order': 9, u'slug': u'beauty'}, u'3': {u'is_parent': -1, u'parent_id': 68, u'is_active': 1, u'id': 10, u'caption': u'\u041a\u0443\u043b\u0438\u043d\u0430\u0440\u0438\u044f', u'order': 20, u'slug': u'cookery'}, u'2': {u'is_parent': -1, u'parent_id': 68, u'is_active': 1, u'id': 113, u'caption': u'\u041c\u044b\u0441\u043b\u0438/\u0446\u0438\u0442\u0430\u0442\u044b', u'order': 21, u'slug': u'fem_thoughts'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 68, u'caption': u'\u0416\u0435\u043d\u0441\u043a\u0438\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', u'order': 10, u'slug': u'girlsclub'}}, u'64': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 64, u'is_active': 1, u'id': 44, u'caption': u'\u041c\u043e\u0442\u043e', u'order': 16, u'slug': u'moto'}, u'0': {u'is_parent': -1, u'parent_id': 64, u'is_active': 1, u'id': 12, u'caption': u'\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438', u'order': 22, u'slug': u'cars'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 64, u'caption': u'\u0410\u0432\u0442\u043e, \u043c\u043e\u0442\u043e', u'order': 10, u'slug': u'auto'}}, u'93': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 93, u'is_active': 1, u'id': 31, u'caption': u'\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438', u'order': 12, u'slug': u'technology'}, u'0': {u'is_parent': -1, u'parent_id': 93, u'is_active': 1, u'id': 34, u'caption': u'\u041f\u043e\u0437\u043d\u0430\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e', u'order': 10, u'slug': u'poznavatelno'}, u'3': {u'is_parent': -1, u'parent_id': 93, u'is_active': 1, u'id': 29, u'caption': u'\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u044b\u0435 \u044f\u0437\u044b\u043a\u0438', u'order': 10, u'slug': u'languages'}, u'2': {u'is_parent': -1, u'parent_id': 93, u'is_active': 1, u'id': 35, u'caption': u'\u041d\u0430\u0443\u043a\u0430', u'order': 5, u'slug': u'science'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 93, u'caption': u'\u041d\u0430\u0443\u043a\u0430 \u0438 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435', u'order': 10, u'slug': u'Sc'}}, u'92': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 92, u'is_active': 1, u'id': 20, u'caption': u'\u041a\u043d\u0438\u0433\u0438', u'order': 5, u'slug': u'books'}, u'0': {u'is_parent': -1, u'parent_id': 92, u'is_active': 1, u'id': 58, u'caption': u'\u0421\u0442\u0438\u0445\u0438', u'order': 20, u'slug': u'stihi'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 92, u'caption': u'\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0438 \u043f\u043e\u044d\u0437\u0438\u044f', u'order': 10, u'slug': u'literature'}}, u'102': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 102, u'is_active': 1, u'id': 30, u'caption': u'\u0413\u043e\u0440\u043e\u0441\u043a\u043e\u043f\u044b', u'order': 10, u'slug': u'horoscope'}, u'0': {u'is_parent': -1, u'parent_id': 102, u'is_active': 1, u'id': 54, u'caption': u'\u0418\u043c\u0435\u043d\u0430', u'order': 5, u'slug': u'names'}, u'2': {u'is_parent': -1, u'parent_id': 102, u'is_active': 1, u'id': 25, u'caption': u'\u041e\u0431\u0440\u0430\u0437 \u0436\u0438\u0437\u043d\u0438', u'order': 7, u'slug': u'lifestyle'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 102, u'caption': u'\u0424\u0438\u043b\u043e\u0441\u043e\u0444\u0438\u044f \u0438 \u044d\u0437\u043e\u0442\u0435\u0440\u0438\u043a\u0430', u'order': 10, u'slug': u'philosophy'}}, u'94': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 94, u'is_active': 1, u'id': 98, u'caption': u'\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u044b', u'order': 14, u'slug': u'computers'}, u'0': {u'is_parent': -1, u'parent_id': 94, u'is_active': 1, u'id': 96, u'caption': u'\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c, \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442', u'order': 10, u'slug': u'mobile'}, u'3': {u'is_parent': -1, u'parent_id': 94, u'is_active': 1, u'id': 97, u'caption': u'\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430, \u0431\u044b\u0442\u043e\u0432\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430', u'order': 12, u'slug': u'electronics'}, u'2': {u'is_parent': -1, u'parent_id': 94, u'is_active': 1, u'id': 23, u'caption': u'\u0413\u0430\u0434\u0436\u0435\u0442\u044b', u'order': 5, u'slug': u'gadgets'}, u'4': {u'is_parent': -1, u'parent_id': 94, u'is_active': 1, u'id': 95, u'caption': u'\u0421\u043e\u0444\u0442', u'order': 10, u'slug': u'Soft'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 94, u'caption': u'\u0422\u0435\u0445\u043d\u0438\u043a\u0430 \u0438 IT', u'order': 10, u'slug': u'tech'}}, u'85': {u'category': {u'1': {u'is_parent': -1, u'parent_id': 85, u'is_active': 1, u'id': 87, u'caption': u'\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u0442\u0434\u044b\u0445', u'order': 10, u'slug': u'active'}, u'0': {u'is_parent': -1, u'parent_id': 85, u'is_active': 1, u'id': 88, u'caption': u'\u0421\u0434\u0435\u043b\u0430\u0439 \u0441\u0430\u043c', u'order': 15, u'slug': u'handmade'}, u'2': {u'is_parent': -1, u'parent_id': 85, u'is_active': 1, u'id': 86, u'caption': u'\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f', u'order': 10, u'slug': u'hobbies'}}, u'group': {u'is_parent': 1, u'parent_id': -1, u'is_active': 1, u'id': 85, u'caption': u'\u041e\u0442\u0434\u044b\u0445', u'order': 10, u'slug': u'rest'}}}, u'private': []}}
    """

    url = 'http://allsocial.ru/common/categories'
    response = requests.get(url)
    json_data = json.loads(response.text)
    json_topicsets = json_data['response']['public']

    topicsets = {} #This will hold all topicsets and topics as follows: {(topicset_id, name): {topic1_id: name, topic2_id: name}}

    #resolve topics without topicsets
    topicsets[('-1', 'Самостоятельные топики')] = {}
    for i in json_topicsets['-1']['category'].keys():
        topic_id = json_topicsets['-1']['category'][i]['id']
        topic_name =  json_topicsets['-1']['category'][i]['caption']
        topicsets[('-1', 'Самостоятельные топики')].update({topic_id: topic_name})
    json_topicsets.pop('-1')

    #resolve all remaining category sets
    for topicset_id in json_topicsets.keys():
        topicset_name = json_topicsets[topicset_id]['group']['caption'].encode('utf-8')
        topicsets[(topicset_id, topicset_name)] = {}
        for i in json_topicsets[topicset_id]['category'].items():
            topic_id = i[1]['id']
            topic_name = i[1]['caption']
            topicsets[(topicset_id,topicset_name)].update({topic_id: topic_name})

    #prints tree of categories for debugging
    # for i in topicsets.keys():
    #     print i[0], i[1]
    #     for t in topicsets[i].items():
    #        print '\t', t[0], t[1].encode('utf-8')

def fill_topic_models():
    """
    Fills two topic-related models
    """

    topicsets = {(u'82', '\xd0\xa1\xd0\xb5\xd0\xbc\xd1\x8c\xd1\x8f \xd0\xb8 \xd0\xb4\xd0\xbe\xd0\xbc'): {40: u'\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f', 83: u'\u0414\u0435\u0442\u0438', 84: u'\u041e\u0431\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u0438 \u0440\u0435\u043c\u043e\u043d\u0442', 38: u'\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', 46: u'\u0421\u0432\u0430\u0434\u0435\u0431\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430'}, (u'85', '\xd0\x9e\xd1\x82\xd0\xb4\xd1\x8b\xd1\x85'): {88: u'\u0421\u0434\u0435\u043b\u0430\u0439 \u0441\u0430\u043c', 86: u'\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f', 87: u'\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u0442\u0434\u044b\u0445'}, ('-1', '\xd0\xa1\xd0\xb0\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xbf\xd0\xb8\xd0\xba\xd0\xb8'): {52: u'\u041c\u043e\u043b\u043e\u0434\u0451\u0436\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', 60: u'\u042e\u043c\u043e\u0440', 4: u'\u041c\u043e\u0434\u0430'}, (u'61', '\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xbb\xd0\xb5\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'): {48: u'\u0412\u0438\u0434\u0435\u043e', 49: u'\u0422\u0435\u043b\u0435\u0432\u0438\u0434\u0435\u043d\u0438\u0435', 53: u'\u0410\u043d\u0438\u043c\u0435/\u0425\u0435\u043d\u0442\u0430\u0439', 7: u'\u041c\u0443\u0437\u044b\u043a\u0430', 41: u'\u041d\u043e\u0441\u0442\u0430\u043b\u044c\u0433\u0438\u044f', 57: u'\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b', 43: u'\u0423\u0436\u0430\u0441\u044b', 5: u'\u041a\u0438\u043d\u043e\u0444\u0438\u043b\u044c\u043c\u044b', 37: u'\u0418\u0433\u0440\u044b'}, (u'89', '\xd0\x98\xd1\x81\xd0\xba\xd1\x83\xd1\x81\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe, \xd0\xb4\xd0\xb8\xd0\xb7\xd0\xb0\xd0\xb9\xd0\xbd'): {16: u'\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438', 19: u'\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', 21: u'\u0418\u043d\u0442\u0435\u0440\u044c\u0435\u0440', 22: u'\u0414\u0438\u0437\u0430\u0439\u043d', 90: u'\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0430', 91: u'\u041b\u0430\u043d\u0434\u0448\u0430\u0444\u0442\u043d\u044b\u0439 \u0434\u0438\u0437\u0430\u0439\u043d'}, (u'103', '\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8b \xd0\xb8 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8'): {112: u'\u0414\u0440\u0443\u0433\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', 24: u'\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u044b', 104: u'\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', 105: u'\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', 106: u'\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435', 107: u'\u0422\u0443\u0440\u0438\u0437\u043c'}, (u'64', '\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe, \xd0\xbc\xd0\xbe\xd1\x82\xd0\xbe'): {12: u'\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438', 44: u'\u041c\u043e\u0442\u043e'}, (u'69', '\xd0\xa1\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82 \xd0\xb8 \xd0\xb7\xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb2\xd1\x8c\xd0\xb5'): {36: u'\u0424\u0443\u0442\u0431\u043e\u043b', 70: u'\u0424\u0438\u0442\u043d\u0435\u0441', 71: u'\u0421\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u043e\u0435 \u043f\u0438\u0442\u0430\u043d\u0438\u0435', 72: u'Workout', 73: u'\u041f\u043e\u0445\u0443\u0434\u0435\u043d\u0438\u0435', 74: u'\u0421\u043f\u043e\u0440\u0442 (\u0434\u0440\u0443\u0433\u043e\u0435)'}, (u'77', '\xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81'): {26: u'\u041c\u043e\u0442\u0438\u0432\u0430\u0446\u0438\u044f', 78: u'\u0424\u0438\u043d\u0430\u043d\u0441\u044b', 79: u'\u0421\u0442\u0430\u0440\u0442\u0430\u043f\u044b'}, (u'94', '\xd0\xa2\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0 \xd0\xb8 IT'): {96: u'\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c, \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442', 97: u'\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430, \u0431\u044b\u0442\u043e\u0432\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430', 98: u'\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u044b', 95: u'\u0421\u043e\u0444\u0442', 23: u'\u0413\u0430\u0434\u0436\u0435\u0442\u044b'}, (u'99', '\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'): {56: u'\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438', 100: u'\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0430', 101: u'\u0413\u0435\u043e\u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0430, \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u043a\u0430', 55: u'\u0420\u0435\u043b\u0438\u0433\u0438\u044f'}, (u'63', '\xd0\x94\xd0\xb5\xd0\xb2\xd1\x83\xd1\x88\xd0\xba\xd0\xb8'): {9: u'\u042d\u0440\u043e\u0442\u0438\u043a\u0430/\u041f\u043e\u0440\u043d\u043e', 39: u'\u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0435 \u0434\u0435\u0432\u0443\u0448\u043a\u0438'}, (u'80', '\xd0\x97\xd0\xbd\xd0\xb0\xd0\xba\xd0\xbe\xd0\xbc\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0 \xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'): {81: u'\u0417\u043d\u0430\u043a\u043e\u043c\u0441\u0442\u0432\u0430', 47: u'\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'}, (u'75', '\xd0\x9f\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0 \xd0\xb8 \xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'): {17: u'\u041f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u044f', 76: u'\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435', 45: u'\u041f\u0440\u0438\u0440\u043e\u0434\u0430'}, (u'102', '\xd0\xa4\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x81\xd0\xbe\xd1\x84\xd0\xb8\xd1\x8f \xd0\xb8 \xd1\x8d\xd0\xb7\xd0\xbe\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0'): {25: u'\u041e\u0431\u0440\u0430\u0437 \u0436\u0438\u0437\u043d\u0438', 54: u'\u0418\u043c\u0435\u043d\u0430', 30: u'\u0413\u043e\u0440\u043e\u0441\u043a\u043e\u043f\u044b'}, (u'92', '\xd0\x9b\xd0\xb8\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0 \xd0\xb8 \xd0\xbf\xd0\xbe\xd1\x8d\xd0\xb7\xd0\xb8\xd1\x8f'): {58: u'\u0421\u0442\u0438\u0445\u0438', 20: u'\u041a\u043d\u0438\u0433\u0438'}, (u'108', '\xd0\xa1\xd0\x9c\xd0\x98, \xd1\x80\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xb0 \xd0\xb8 PR'): {32: u'\u0420\u0435\u043a\u043b\u0430\u043c\u0430', 33: u'\u0417\u043d\u0430\u043c\u0435\u043d\u0438\u0442\u043e\u0441\u0442\u0438', 6: u'\u0421\u041c\u0418'}, (u'68', '\xd0\x96\xd0\xb5\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0'): {113: u'\u041c\u044b\u0441\u043b\u0438/\u0446\u0438\u0442\u0430\u0442\u044b', 10: u'\u041a\u0443\u043b\u0438\u043d\u0430\u0440\u0438\u044f', 13: u'\u041a\u0440\u0430\u0441\u043e\u0442\u0430', 15: u'\u0414\u0438\u0435\u0442\u044b'}, (u'93', '\xd0\x9d\xd0\xb0\xd1\x83\xd0\xba\xd0\xb0 \xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'): {34: u'\u041f\u043e\u0437\u043d\u0430\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e', 35: u'\u041d\u0430\u0443\u043a\u0430', 29: u'\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u044b\u0435 \u044f\u0437\u044b\u043a\u0438', 31: u'\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438'}, (u'109', '\xd0\xa0\xd0\xb5\xd0\xb3\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0'): {59: u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430', 50: u'\u0420\u043e\u0441\u0441\u0438\u044f', 27: u'\u0420\u0435\u0433\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0430', 114: u'\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d', 110: u'\u041a\u0430\u0432\u043a\u0430\u0437\u0441\u043a\u0438\u0435'}}

    for key in topicsets.keys():
        if key[0] is not '-1': #topics outside of any topicset
            _gts = GroupTopicSet.objects.create(id=key[0], name=key[1])
            for topic in topicsets[key]:
                _gts.grouptopic_set.create(id=topic, name=topicsets[key][topic] , grouptopicset=key[0])
        else:
            for topic in topicsets[key]:
                GroupTopic.objects.create(id=topic, name=topicsets[key][topic])

def parse_to_model():
    """
    Gets data from allsocial.ru
    Prepares dictionaries and fills required models
    """

    total_count = json.loads(requests.get('http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=204924&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1').text)['response']['total_count']
    # total_pages = total_count / 25 + 1 #number of requests. one response carries 25 entries

    #for testing purposes
    total_pages = 4

    #get all responses from allsocial
    for page in range(total_pages):

        #print how many communities are already parsed
        print '%s groups in db' % GroupAdditionalData.objects.count()

        #get response from the server and load data
        offset = page*25
        url = 'http://allsocial.ru/entity?direction=1&is_closed=-1&is_verified=-1&list_type=1&offset=' + str(offset) + '&order_by=quantity&period=month&platform=1&range=0:8000000&type_id=-1'
        response = requests.get(url)
        json_data = json.loads(response.text)

        #each response holds data for 25 communities
        for i in range(25):
            group = json_data['response']['entity'][i]

            #dictionary is returned and has to be tweaked to fit into models
            #removing excess data
            toremove = ['diff_abs', 'diff_rel', 'can_change_cpp', 'id']
            for i in toremove:
                if i in group.keys():
                    group.pop(i)
                else:
                    print "%s not in response keys" % i #That means something went wrong :(
                    return

            #renaming response fields to match Group model
            group['remote_id'] = group.pop('vk_id')
            group['members_count'] = group.pop('quantity')
            group['photo_big'] = group.pop('avatar')
            group['type'] = group.pop('type_id')
            group['name'] = group.pop('caption')
            group['verified'] = group.pop('is_verified')

            #creating dictionary to later decode to Group Statistics model
            statistics = {}
            statistics['reach'] = group.pop('reach')
            statistics['visitors'] = group.pop('visitors')
            statistics['group'] = group['remote_id']
            statistics['date'] = datetime.today()

            #creating dictionary to later decode to GroupAdditionalData model
            groupadditionaldata = {}
            _topics = group.pop('category')
            groupadditionaldata['vk_id'] = group['remote_id']
            groupadditionaldata['date'] = datetime.today()
            groupadditionaldata['in_search'] = group.pop('in_search')
            groupadditionaldata['cpp'] = group.pop('cpp')

            #sending data sets to models
            g = Group.objects.create(**group)
            g.save()
            statistics['group'] = g
            GroupStatistic.objects.create(**statistics)
            groupadditionaldata['vk_id'] = g
            gad = GroupAdditionalData.objects.create(**groupadditionaldata)
            gad.grouptopics = _topics.keys()

fill_topic_models()
parse_to_model()
