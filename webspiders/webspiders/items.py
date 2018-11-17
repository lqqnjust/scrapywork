# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanTopic(scrapy.Item):
    """
    豆瓣话题信息
    """
    # 标题
    title = scrapy.Field()
    # url
    url = scrapy.Field()
    # author_name 
    author_name = scrapy.Field()
    author_url = scrapy.Field()
    group_id = scrapy.Field()
    group_name = scrapy.Field()
    

