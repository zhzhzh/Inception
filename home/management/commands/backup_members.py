from django.core.management.base import BaseCommand
from home.models import Member
import sys
from pandas import DataFrame
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf8')

class Command(BaseCommand):
    def handle(self, *args, **options):
        member_list = []
        members = Member.objects.all()
        for member in members:
            member_list.append(member.as_json())

        df = DataFrame(member_list)
        df.to_csv('members.csv')
        pprint(df)


        print('Done')