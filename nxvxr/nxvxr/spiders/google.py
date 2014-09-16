'''
Example of Scrapy spider used for scraping the google url.
Not actual running code.
'''
import re
import os
import sys
import json
 
from scrapy.spider import Spider
from scrapy.selector import Selector
 
class GoogleSearch(Spider):
    #set the search result here
    name = 'google'
    allowed_domains = ['www.google.com']
    query = 'inurl%3Ahttps%3A%2F%2Fwatcha.net%2Fm%2Fmv%2F+-staffs'
    start_urls = ['https://www.google.com/search?q=%s&num=100&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb' % query]

    def parse(self, response):
        sel = Selector(response)
        google_search_links_list = sel.xpath('//h3/a/@href').extract()
        google_search_links_list = [re.search('q=(.*)&sa',n).group(1) for n in google_search_links_list]

        with open('google.json', "w") as outfile:
            json.dump({'output_url':google_search_links_list}, outfile, indent=4)
