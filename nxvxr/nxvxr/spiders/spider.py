__author__ = 'carpedm20'
__date__ = '2014.09.15'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

import urlparse
import json
import re
from scrapy.item import Item, Field
from scrapy import Request
from scrapy.spider import Spider

# CONCURRENT_REQUESTS
# http://m.movie.naver.com/m/endpage/movie/PointListJson.nhn?movieCode=116532&page=6&target=after&onlyActualPoint=false&order=sympathyScore
# after : after release
# before : before release
# onlyActualPoint : 

with open('total_movie_list.json') as f:
    movie_dict = json.loads(f.read())

movie_codes = [url[url.find('code=')+5:] for url in movie_dict.keys()]

BASE_URL = "http://m.movie.naver.com/m/endpage/movie/PointListJson.nhn?movieCode=%s&target=%s&onlyActualPoint=%s&order=sympathyScore&page=0"

onlyActualPoint = 'false'

after_movie_urls = [BASE_URL % (code, 'after', onlyActualPoint) for code in movie_codes]
before_movie_urls = [BASE_URL % (code, 'before', onlyActualPoint) for code in movie_codes]

class Review(Item):
    # define the fields for your item here like:
    code = Field()
    point = Field()
    text = Field()
    #is_viewer = Field()
    is_after = Field()

    nickname = Field()
    encrypted_id = Field()

    pos = Field()
    neg = Field()
    date = Field()

    def __str__(self):
        return "[%s] %s" % (self.code, self.page)

class NxvxrSpider(Spider):
    name = "nxvxr"
    allowed_domains = ["naver.com"]
    #start_urls = after_movie_urls + before_movie_urls
    #start_urls = after_movie_urls[:3]
    start_urls = []

    def __init__(self, start_index='0'):
        self.start_index = int(start_index)

        urls = after_movie_urls + before_movie_urls
        s_idx = len(urls)/20 * self.start_index
        e_idx = len(urls)/20 * (self.start_index + 1)

        if start_index != '19':
            self.start_urls = urls[s_idx:e_idx]
        else:
            self.start_urls = urls[s_idx:]

    def parse(self, response):
        print response.url
        if not response.body.strip():
            return

        parsed = urlparse.urlparse(response.url)
        code = urlparse.parse_qs(parsed.query)['movieCode'][0]
        is_after = urlparse.parse_qs(parsed.query)['target'][0]
        page = int(urlparse.parse_qs(parsed.query)['page'][0])

        base_url = response.url[:response.url.rfind('=')]

        hxs = HtmlXPathSelector(response)
        movies = hxs.xpath("//li/span")

        yield Request(base_url+"="+str(page+1))

        for movie in movies:
            point = int(movie.xpath('.//strong/text()')[0].extract())
            text = movie.xpath('.//span[@class="wn wh4"]/text()')[0].extract().encode('utf-8').strip()

            nick = movie.xpath('.//span[@class="tx3"]/text()')[0].extract().encode('utf-8').strip()
            nickname = ""
            if "****" in nick:
                encrypted_id = nick[nick.find('(')+1:-1]
                nickname = nick[:nick.find('(')]
            else:
                encrypted_id = nick

            pos = int(movie.xpath('.//a[@class="_sympathyButton"]/em/text()')[0].extract())
            neg = int(movie.xpath('.//a[@class="_notSympathyButton"]/em/text()')[0].extract())

            date = movie.xpath('.//span[@class="tx4"]/text()')[0].extract().replace('  ',' ')

            review = Review()
            review['code'] = code
            review['point'] = point
            review['text'] = text
            review['is_after'] = is_after
            review['nickname'] = nickname
            review['encrypted_id'] = encrypted_id
            review['pos'] = pos
            review['neg'] = neg
            review['date'] = date

            yield review
