__author__ = 'jzhang14'

import os
import sys

dir_name = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir_name, os.path.pardir))
sys.path.append(parent_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Inception.settings'
import django
django.setup()

from home.models import Member
Member.objects.all().delete()
Member.objects.bulk_create([
    Member(name='', name_ch='', nick_name='', number=1,
           pos1='', pos2='', pos3='',
           level=0, balance=0, physique=0, bug=0),
    Member(name='', name_ch='', nick_name='', number=1,
           pos1='', pos2='', pos3='',
           level=0, balance=0, physique=0, bug=0),
])

print('Done')
