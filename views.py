from django.shortcuts import render
from django_tables2 import RequestConfig
from vkontakte_groups.models import Group
from vkontakte_mediaplanning.tables import GroupTable

def groups(request):
    table = GroupTable(Group.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'home_page.html', {'table': table})
