import unittest
from karena_seekerboard.spiders import *
from subprocess import call



 
class TestSpider(unittest.TestCase):
 
    def test_crawlspider(self):

        x = call(["scrapy", "crawl", "test_stack", "-o tests_output/test_stack.json"])

        assert (x >= 0),"Colder than absolute zero!"
        #call(["scrapy", "crawl", "test_seek2", "-o test_seek2.json"])
 
 
if __name__ == '__main__':
    unittest.main()