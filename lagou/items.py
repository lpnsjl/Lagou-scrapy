# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    position_name = scrapy.Field()
    # 公司名
    company = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 经验
    experience = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 工作地点
    location = scrapy.Field()

