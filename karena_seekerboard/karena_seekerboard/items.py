# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KarenaSeekerboardItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    jobtitle = scrapy.Field()
    company = scrapy.Field()
    joblink = scrapy.Field()
    advertised_date = scrapy.Field(serializer=str)
    
