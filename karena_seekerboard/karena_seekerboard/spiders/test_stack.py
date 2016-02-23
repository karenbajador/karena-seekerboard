import logging

from karena_seekerboard.spiders import StackSpider
from scrapy.selector import Selector
from karena_seekerboard.items import KarenaSeekerboardItem


class TestStackSpider(StackSpider):

	pipeline = set([])
	name = "test_stack"
    
	def __init__(self):
		self.test = True



         
          
    
    
	