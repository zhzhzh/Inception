import os
from pprint import pprint

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from pandas import DataFrame

from home.models import Member


class Command(BaseCommand):
    def handle(self, *args, **options):
        member_file = settings.MEMBER_FILE
        if not os.path.isfile(member_file):
            print('{} file not exists!'.format(member_file))

        df = DataFrame.from_csv(member_file)

        member_list = []
        pprint(df)

        for index, row in df.iterrows():
            if pd.isnull(index):
                continue

            print('-' * 64)
            print(index)
            # pprint(row)
            member = Member(
                name=row['name'],
                name_chn=row['name_chn'],
                nick_name=row['nick_name'],
                number=row['number'],
                pos1='' if pd.isnull(row['pos1']) else row['pos1'],
                pos2='' if pd.isnull(row['pos2']) else row['pos2'],
                pos3='' if pd.isnull(row['pos3']) else row['pos3'],
                top_star=row['top_star'],
                all_pos=row['all_pos'],
                stamina=row['stamina'],
                athletic=row['athletic'],
                grade=row['grade']
            )
            pprint(member.as_json())
            member_list.append(member)

        if len(member_list) > 0:
            Member.objects.all().delete()
            Member.objects.bulk_create(member_list)

        print('Done')
