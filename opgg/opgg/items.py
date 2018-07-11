# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpggItem(scrapy.Item):
    Top3NickName = scrapy.Field()
    Top3Rating = scrapy.Field()
    Top3Matches = scrapy.Field()
    Top3WinRate = scrapy.Field()
    Top3TenRate = scrapy.Field()
    Top3Kda = scrapy.Field()
    Top3Damage = scrapy.Field()
    Top3AvgRank = scrapy.Field()
    Index = scrapy.Field()
    Serv_name = scrapy.Field()
    
    
