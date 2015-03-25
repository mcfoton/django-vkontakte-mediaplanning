import django_tables2 as tables
from vkontakte_groups.models import Group

class GroupTable(tables.Table):
    class Meta:
        model = Group
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ('name', 'verified', 'members_count')
