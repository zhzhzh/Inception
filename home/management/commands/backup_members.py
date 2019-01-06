from django.core.management.base import BaseCommand
from home.models import Member
import sys
from pandas import DataFrame
from pprint import pprint
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        reload(sys)
        sys.setdefaultencoding('utf8')

        member_list = []
        members = Member.objects.all()
        for member in members:
            member_list.append(member.as_json())

        df = DataFrame(member_list)
        pprint(df)

        df.to_csv(settings.MEMBER_FILE)

        print('Done')
