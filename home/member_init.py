# -*- coding:utf-8 -*-

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
    Member(name='chen', name_chn='陈华', nick_name='陈老师', number=1,
           pos1='守门员', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=3),
    Member(name='ben', name_chn='俞斌辉', nick_name='本本', number=2,
           pos1='攻击型中场', pos2='防守型中场', pos3='中后卫',
           top_star=0, all_pos=1, stamina=1, athletic=1, grade=5),
    Member(name='arthur', name_chn='余刚', nick_name='阿色', number=3,
           pos1='边后卫', pos2='中后卫', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=6),
    Member(name='vincent', name_chn='胡焱钧', nick_name='文森特', number=4,
           pos1='边后卫', pos2='攻击型中场', pos3='守门员',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='symon', name_chn='陶晓鸣', nick_name='西门', number=5,
           pos1='中后卫', pos2='边后卫', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=6),
    Member(name='tao', name_chn='陶新', nick_name='华弟', number=6,
           pos1='攻击型中场', pos2='防守型中场', pos3='防守型中场',
           all_pos=0, stamina=0, top_star=0, athletic=0, grade=7),
    Member(name='rick', name_chn='许英俊', nick_name='里克', number=7,
           pos1='攻击型中场', pos2='边后卫', pos3='',
           top_star=0, all_pos=1, stamina=1, athletic=0, grade=5),
    Member(name='rp', name_chn='朱律均', nick_name='人品', number=8,
           pos1='前锋', pos2='攻击型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=5),
    Member(name='sky', name_chn='吕旻', nick_name='天天', number=9,
           pos1='攻击型中场', pos2='防守型中场', pos3='防守型中场',
           top_star=1, all_pos=1, stamina=1, athletic=0, grade=2),
    Member(name='dong', name_chn='董培青', nick_name='董', number=10,
           pos1='攻击型中场', pos2='防守型中场', pos3='前锋',
           top_star=1, all_pos=1, stamina=1, athletic=1, grade=2),
    Member(name='derek', name_chn='王景东', nick_name='德里克', number=11,
           pos1='边后卫', pos2='攻击型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=6),
    Member(name='wallace', name_chn='黄文钧', nick_name='华莱士', number=12,
           pos1='防守型中场', pos2='中后卫', pos3='攻击型中场',
           top_star=1, all_pos=1, stamina=1, athletic=0, grade=4),
    Member(name='j8', name_chn='姚俊', nick_name='姚俊', number=13,
           pos1='防守型中场', pos2='中后卫', pos3='攻击型中场',
           top_star=0, all_pos=1, stamina=0, athletic=1, grade=7),
    Member(name='master', name_chn='刘卓', nick_name='大师', number=14,
           pos1='前锋', pos2='边后卫', pos3='攻击型中场',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='wu', name_chn='吴宇华', nick_name='线裤', number=15,
           pos1='中后卫', pos2='边后卫', pos3='防守型中场',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=4),
    Member(name='allen', name_chn='王志合', nick_name='艾伦', number=16,
           pos1='边后卫', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='meixi', name_chn='刘光巍', nick_name='霉西', number=17,
           pos1='特殊', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
    Member(name='qiuba', name_chn='张朝元', nick_name='球霸', number=18,
           pos1='前锋', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=1),
    Member(name='yh', name_chn='严慧', nick_name='鞋魔', number=19,
           pos1='边后卫', pos2='中后卫', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
    Member(name='joseph', name_chn='金骁骅', nick_name='色夫', number=20,
           pos1='守门员', pos2='前锋', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=3),
    Member(name='baogang', name_chn='李宝刚', nick_name='宝刚', number=21,
           pos1='前锋', pos2='攻击型中场', pos3='',
           top_star=1, all_pos=0, stamina=0, athletic=1, grade=2),
    Member(name='xuxu', name_chn='徐增雨', nick_name='哪吒', number=22,
           pos1='前锋', pos2='攻击型中场', pos3='',
           top_star=1, all_pos=0, stamina=1, athletic=0, grade=2),
    Member(name='xu', name_chn='徐斌', nick_name='徐老师', number=23,
           pos1='边后卫', pos2='中后卫', pos3='防守型中场',
           top_star=0, all_pos=1, stamina=0, athletic=0, grade=6),
    Member(name='brother', name_chn='沈斌', nick_name='阿哥', number=24,
           pos1='守门员', pos2='前锋', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=3),
    Member(name='tiejun', name_chn='白铁军', nick_name='铁军', number=25,
           pos1='中后卫', pos2='防守型中场', pos3='边后卫',
           top_star=0, all_pos=1, stamina=1, athletic=0, grade=4),
    Member(name='alson', name_chn='', nick_name='Alson', number=26,
           pos1='攻击型中场', pos2='防守型中场', pos3='边后卫',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=6),
    Member(name='captain', name_chn='王晓铭', nick_name='队长', number=27,
           pos1='前锋', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=1),
    Member(name='henry', name_chn='黄毅', nick_name='亨利', number=28,
           pos1='防守型中场', pos2='边后卫', pos3='中后卫',
           top_star=0, all_pos=1, stamina=0, athletic=0, grade=6),
    Member(name='lin', name_chn='林舜宇', nick_name='小林', number=32,
           pos1='攻击型中场', pos2='边后卫', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='miba', name_chn='陈述', nick_name='米霸', number=38,
           pos1='中后卫', pos2='防守型中场', pos3='攻击型中场',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=6),
    Member(name='tarou', name_chn='谭芃', nick_name='太郎', number=39,
           pos1='边后卫', pos2='前锋', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='chang', name_chn='常力鹏', nick_name='柱子', number=40,
           pos1='防守型中场', pos2='中后卫', pos3='边后卫',
           top_star=0, all_pos=0, stamina=1, athletic=1, grade=7),
    Member(name='hua', name_chn='殷华', nick_name='华仔', number=42,
           pos1='中后卫', pos2='防守型中场', pos3='攻击型中场',
           top_star=0, all_pos=1, stamina=1, athletic=0, grade=7),
    Member(name='sprite', name_chn='王金亮', nick_name='金亮', number=81,
           pos1='中后卫', pos2='防守型中场', pos3='边后卫',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=4),
    Member(name='xiaop', name_chn='汪远', nick_name='小P', number=88,
           pos1='边后卫', pos2='攻击型中场', pos3='防守型中场',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=6),
    Member(name='hao', name_chn='刘豪', nick_name='小舅子', number=90,
           pos1='攻击型中场', pos2='前锋', pos3='防守型中场',
           top_star=1, all_pos=0, stamina=1, athletic=1, grade=5),
    Member(name='eric', name_chn='汪健', nick_name='艾里克', number=99,
           pos1='边后卫', pos2='防守型中场', pos3='攻击型中场',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
    Member(name='tieta', name_chn='', nick_name='铁塔', number=101,
           pos1='防守型中场', pos2='攻击型中场', pos3='',
           top_star=1, all_pos=0, stamina=0, athletic=1, grade=2),
    Member(name='elvin', name_chn='', nick_name='艾尔文', number=101,
           pos1='防守型中场', pos2='攻击型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
    Member(name='flemming', name_chn='', nick_name='弗莱明', number=45,
           pos1='攻击型中场', pos2='边后卫', pos3='防守型中场',
           top_star=1, all_pos=1, stamina=0, athletic=1, grade=5),
    Member(name='wood', name_chn='', nick_name='木吒', number=101,
           pos1='攻击型中场', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='gold', name_chn='', nick_name='金吒', number=101,
           pos1='防守型中场', pos2='攻击型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=1, grade=7),
    Member(name='blue', name_chn='王逸洲', nick_name='蓝少', number=101,
           pos1='攻击型中场', pos2='边后卫', pos3='防守型中场',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=5),
    Member(name='wind', name_chn='李靓', nick_name='枭风', number=101,
           pos1='特殊', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
    Member(name='gorden', name_chn='顾剑锋', nick_name='戈登', number=101,
           pos1='攻击型中场', pos2='攻击型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=5),
    Member(name='fish', name_chn='', nick_name='小鱼', number=101,
           pos1='防守型中场', pos2='', pos3='前锋',
           top_star=1, all_pos=1, stamina=1, athletic=1, grade=2),
    Member(name='dap', name_chn='', nick_name='大派', number=101,
           pos1='攻击型中场', pos2='防守型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=2),
    Member(name='le', name_chn='', nick_name='阿乐', number=101,
           pos1='攻击型中场', pos2='防守型中场', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='tim', name_chn='', nick_name='蒂姆', number=101,
           pos1='特殊', pos2='', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=7),
    Member(name='ball', name_chn='许敏', nick_name='球球', number=101,
           pos1='中后卫', pos2='防守型中场', pos3='边后卫',
           top_star=0, all_pos=1, stamina=0, athletic=0, grade=6),
    Member(name='kevin', name_chn='裔立峰', nick_name='凯文', number=101,
           pos1='攻击型中场', pos2='边后卫', pos3='',
           top_star=0, all_pos=0, stamina=0, athletic=0, grade=8),
])

print('Done')
