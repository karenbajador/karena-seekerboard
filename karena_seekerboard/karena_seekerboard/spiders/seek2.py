# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By

from karena_seekerboard.items import KarenaSeekerboardItem


class Seek2Spider(scrapy.Spider):
    name = "seek2"
    allowed_domains = ["http://www.seek.com.au/"]
    start_urls = (
        'http://www.seek.com.au/',
    )

    def start_requests(self):
    	driver = webdriver.PhantomJS()
    	# go to the home page
    	driver.get('http://www.seek.com.au/')

    	form_element = driver.find_element_by_xpath("//form[@id='layout']")
    	keywords = driver.find_element_by_xpath("//input[@id='keywords']")
    	classification = driver.find_element_by_xpath("//select[@id='classification']")
    	subclassification = driver.find_element_by_xpath("//select[@id='subclassification']")
    	where = driver.find_element_by_xpath("//input[@id='where']")

    	keywords.send_keys('python')
    	classification.send_keys('6281')
        subclassification.send_keys('6290')
        where.send_keys('Melbourne CBD & Inner Suburbs Melbourne VIC')

    	form_element.submit()

    	yield scrapy.Request(driver.current_url,self.parse)

    	driver.close()



    def parse(self, response):



		jobs_listing = response.xpath("//div[@class='jobs-list jobs-list-primary']").extract()
		self.logger.info("jobs_listing>>>>>>>>>>>>>>>>>>>>>> %s" % jobs_listing)

		for jobs in jobs_listing:
			self.logger.info("jobs>>>>>>>>>>>>>>>>>>>>>> %s" % jobs)
        	
        	
        	item = KarenaSeekerboardItem()
        	# item['jobtitle'] = jobs.xpath(
         #        '//a[@class="job-title"]/text()').extract()[0]
        	# item['joblink'] = jobs.xpath(
         #        '//a[@class="job-title"]/@href').extract()[0]
        	yield item