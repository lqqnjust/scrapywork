# coding:utf-8
from django.db import models

# Create your models here.


class Profile(models.Model):
    nickname = models.CharField(u"昵称", max_length=32)
    profile_url = models.URLField(u'主页地址')

    def __str__(self):
        return self.nickname


class Task(models.Model):
    name = models.CharField(u'任务名称', max_length=32)
    timetype = models.CharField(u'时间类型', max_length=32)
    config = models.TextField(u'参数配置')
    spiderclass = models.CharField(u'爬虫类名', max_length=32)

    def __str__(self):
        return self.name


