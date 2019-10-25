# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    # 爬虫入口 会将这个扔到调度器里面去
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//div[@class='indent']//table//tr[@class='item']")
        for i in movie_list:
            douban_item = DoubanItem()
            douban_item['movie_name'] = ''.join(i.xpath(
                ".//td[@valign='top']//div//a/text()").extract_first().split()) + i.xpath(
                ".//td[@valign='top']//div//a/span/text()").extract_first()
            douban_item['describe'] = i.xpath(
                ".//td[@valign='top']//div//p[@class='pl']/text()").extract_first()
            douban_item['star'] = i.xpath(
                ".//td[@valign='top']//div//div[@class='star clearfix']//span[@class='rating_nums']/text()").extract_first()
            douban_item['evaluate'] = i.xpath(
                ".//td[@valign='top']//div//div[@class='star clearfix']//span[@class='pl']/text()").extract_first()
            yield douban_item
            print(douban_item)