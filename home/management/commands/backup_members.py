import sys
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand
from pandas import DataFrame

from home.models import Member


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
