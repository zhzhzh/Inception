from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=32, null=False)
    nick_name = models.CharField(max_length=32, unique=True, null=False)
    number = models.IntegerField(null=True)
    pos_first = models.CharField(max_length=32, null=False)
    pos_second = models.CharField(max_length=32, null=True)
    pos_third = models.CharField(max_length=32, null=True)
    level = models.BooleanField(default=False)
    balance = models.BooleanField(default=False)
    physique = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nick_name + ' - ' + str(self.number) + ' - ' + self.pos_first
