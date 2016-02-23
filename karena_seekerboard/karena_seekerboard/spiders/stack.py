# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector

from karena_seekerboard.items import KarenaSeekerboardItem


class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://stackoverflow.com/questions?pagesize=50&sort=newest',
    )

    def __init__(self):
    	self.test = False


    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        if self.test:
        	questions = [questions[0]]

        print "questions: %s" % questions

        for question in questions:
            item = KarenaSeekerboardItem()
            item['jobtitle'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['joblink'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]

            self.logger.info("item >  >   >   >> %s" % item)
            print "item >  >   >   >> %s" % item

         
            yield item