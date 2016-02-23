import scrapy
import hashlib
from scrapy.selector import Selector
from karena_seekerboard.items import KarenaSeekerboardItem
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

class SeekSpider(scrapy.Spider):

	name = 'seek'
	allowed_domains = ['http://www.seek.com.au/']
	start_urls = ['http://www.seek.com.au/']
	filter_data =  {
		'keyword' : 'python',
		'classification' : '6281', # Information & Communication Technology
		'subclassification' : '6290', # Engineering Software
		'where' : 'Melbourne CBD & Inner Suburbs Melbourne VIC',
	}
	start_urls = ['http://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-melbourne-cbd-inner-suburbs-melbourne-vic/#dateRange=999&workType=0&industry=6281&occupation=6290&graduateSearch=false&salaryFrom=0&salaryTo=999999&salaryType=annual&companyID=&advertiserID=&advertiserGroup=&keywords=python&page=1&displaySuburb=&seoSuburb=&where=Melbourne+CBD+%26+Inner+Suburbs+Melbourne+VIC&whereId=5069&whereIsDirty=false&isAreaUnspecified=false&location=1002&area=5069&nation=&sortMode=KeywordRelevance&searchFrom=quick&searchType=']

	# def __init__(self, start_urls=None):
		#self.start_urls = ['http://www.seek.com.au/']


	# def __init__(self, category=None, *args, **kwargs):

	# 	super(SeekSpider, self).__init__(*args, **kwargs)

	# 	self.logger.info('>>>>>>>>>>>>>>>>> INIT!!!!!')
	# 	self.logger.info('>>>>>>>>>>>>>>>>> INIT!!!!!')
	# 	self.logger.info('>>>>>>>>>>>>>>>>> INIT!!!!!')
       
        
 #        self.allowed_domains = ['http://www.seek.com.au/']
 #        self.start_urls = ['http://www.seek.com.au/']

 #        # Replace hardcoded values below with variables
 #        self.filter_data =  {
	# 		'keyword' : 'python',
	# 		'classification' : '6281', # Information & Communication Technology
	# 		'subclassification' : '6290', # Engineering Software
	# 		'where' : 'Melbourne CBD & Inner Suburbs Melbourne VIC',
	# 	}

	# def start_requests(self):

	# 	self.logger.info('>>>>>>>>>>>>>>>>> START REQUESTS!!!!!')
	# 	self.logger.info('>>>>>>>>>>>>>>>>> START REQUESTS!!!!!')
	# 	self.logger.info('>>>>>>>>>>>>>>>>> START REQUESTS!!!!!')

    	# Create a new instance of the Firefox driver
    	# driver = webdriver.Firefox()
    	# go to the home page
    	# driver.get(start_urls)

    	# form_element = driver.find_elements(By.XPATH, "//form[@id='layout']")

    	

    	# keywords = driver.find_elements(By.XPATH, "//input[@id='keywords']")

    	# print('>>>>>>>>>>>>>>>>> keyword: %s' % keywords)


    	# classification = driver.find_elements(By.XPATH, "//select[@id='classification']")
    	# subclassification = driver.find_elements(By.XPATH, "//select[@id='subclassification']")
    	# where = driver.find_elements(By.XPATH, "//input[@id='where']")
		#button = driver.find_elements(By.XPATH, "//button[@class='seek-button--primary']")

        # keywords.send_keys(filter_data['keyword'])
        # classification.send_keys(filter_data['classification'])
        # subclassification.send_keys(filter_data['subclassification'])
        # where.send_keys(filter_data['where'])
        # #button.click()
        # form_element.submit()

        # scrapy.Request(driver.current_url, self.parse)
        # start_urls = ['http://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-melbourne-cbd-inner-suburbs-melbourne-vic/#dateRange=999&workType=0&industry=6281&occupation=6290&graduateSearch=false&salaryFrom=0&salaryTo=999999&salaryType=annual&companyID=&advertiserID=&advertiserGroup=&keywords=python&page=1&displaySuburb=&seoSuburb=&where=Melbourne+CBD+%26+Inner+Suburbs+Melbourne+VIC&whereId=5069&whereIsDirty=false&isAreaUnspecified=false&location=1002&area=5069&nation=&sortMode=KeywordRelevance&searchFrom=quick&searchType=']
        # start_urls = ['http://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-melbourne-cbd-inner-suburbs-melbourne-vic/#dateRange=999&workType=0&industry=6281&occupation=6290&graduateSearch=false&salaryFrom=0&salaryTo=999999&salaryType=annual&companyID=&advertiserID=&advertiserGroup=&keywords=python&page=1&displaySuburb=&seoSuburb=&where=Melbourne+CBD+%26+Inner+Suburbs+Melbourne+VIC&whereId=5069&whereIsDirty=false&isAreaUnspecified=false&location=1002&area=5069&nation=&sortMode=KeywordRelevance&searchFrom=quick&searchType=']
        # driver.close()

#jobsListing > div.jobs-list.jobs-list-primary > article:nth-child(1)
#//*[@id="jobsListing"]/div[3]/article[1]

	def parse(self, response):
		self.logger.info('PARSE!!!!!!!!!!!!!!!!!!!!!')
		self.logger.info('extract>>>>>>> %s' % response.selector.xpath('//article').extract())
		
		for job_item in response.selector.xpath('//article').extract():
			self.logger.info('job_item>>>>>>>>>> %s', job_item)
			# self.parse_item(sel=Selector(text=job_item))


        # next_page_url = response.selector.xpath("//dd[@class='next-page']/a/@href").extract()
        # if next_page:
        # 	url = response.urljoin(next_page_url)
        # 	yield scrapy.Request(url, self.parse)

    

	# def parse_item(self, sel=None):
	# 	self.logger.info('Hi, this is an item page! %s', response.url)
 #        item = scrapy.KarenaSeekerboardItem()
        
 #        item['title'] = sel.xpath('//a[@class="job-title"]/text()').extract()
 #        item['link'] = sel.xpath('//a[@class="job-title"]/@href').extract()

 #        item['id'] = hashlib.md5(item['link']).hexdigest()

 #        item['company'] = sel.xpath('//em[@class="advertiser-name"]/text()').extract()
 #        item['advertised_date'] = sel.xpath('//span[@class="listing-date"]/text()').extract()
        
        
        




#Constructing from text:

# >>> body = '<html><body><span>good</span></body></html>'
# >>> Selector(text=body).xpath('//span/text()').extract()
# [u'good']

# scrapy runspider myspider.py

# scrapy crawl karena_seekerboard - run on top level of project folder

# Trying out selectors
# scrapy shell "http://www.seek.com.au/"

# Storing in json
# scrapy crawl dmoz -o items.json

# Generate a new Spider
# scrapy genspider mydomain mydomain.com

# Deployig scrapy
# scrapyd-deploy

# Spider arguments
# scrapy crawl myspider -a category=electronics

# Good scraping tutorial
# http://gabrielelanaro.github.io/blog/2015/04/24/scraping-data.html


seek = SeekSpider()

