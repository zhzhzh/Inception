# -*- coding:utf-8 -*-
from django.db import models


class Member(models.Model):
    POS_CHOICES = (
        ('守门员', '守门员'),
        ('中后卫', '中后卫'),
        ('边后卫', '边后卫'),
        ('防守型中场', '防守型中场'),
        ('攻击型中场', '攻击型中场'),
        ('前锋', '前锋'),
    )

    name = models.CharField(max_length=32, null=False)
    name_chn = models.CharField(max_length=32, null=False, verbose_name='姓名')
    nick_name = models.CharField(max_length=32, unique=True, null=False, verbose_name='昵称')
    number = models.IntegerField(null=True, verbose_name='号码')
    pos1 = models.CharField(max_length=32, null=False, choices=POS_CHOICES, verbose_name='第一位置')
    pos2 = models.CharField(max_length=32, null=True, choices=POS_CHOICES, verbose_name='第二位置')
    pos3 = models.CharField(max_length=32, null=True, choices=POS_CHOICES, verbose_name='第三位置')
    balance = models.BooleanField(default=False, verbose_name='天王巨星')
    level = models.BooleanField(default=False, verbose_name='体能狂魔')
    physique = models.BooleanField(default=False, verbose_name='体格达人')

    class Meta:
        db_table = 'member'
        ordering = ['number']

    def __unicode__(self):
        if self.number < 100:
            return str(self.number) + '.' + self.nick_name
        else:
            return self.nick_name

