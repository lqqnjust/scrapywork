# coding:utf-8
from django.db import models

# Create your models here.


class Profile(models.Model):
    nickname = models.CharField(u"昵称", max_length=32)
    profile_url = models.URLField(u'主页地址')

    def __str__(self):
        return self.nickname