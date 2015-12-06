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
    Member(name='chen', name_ch='陈华', nick_name='陈老师', number=1,
           pos1='守门员', pos2='', pos3='',
           level=0, balance=0, physique=0, bug=0),
    Member(name='ben', name_ch='俞斌辉', nick_name='本本', number=2,
           pos1='防守型中场', pos2='中后卫', pos3='攻击型中场',
           level=1, balance=0, physique=1, bug=0),
])

print('Done')
