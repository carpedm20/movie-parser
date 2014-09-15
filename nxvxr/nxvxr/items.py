# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NxvxrItem(scrapy.Item):
    # define the fields for your item here like:
    movie_title = scrapy.Field()
    movie_id = scrapy.Field()

    point = scrapy.Field()
    is_viewer = scrapy.Field()

    text = scrapy.Field()

    nickname = scrapy.Field()
    encrypted_id = scrapy.Field()

    pos = scrapy.Field()
    neg = scrapy.Field()

    date = scrapy.Field()
