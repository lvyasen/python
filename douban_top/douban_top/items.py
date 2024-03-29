# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()
    introduce = scrapy.Field()
    movie_name = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    describe = scrapy.Field()
