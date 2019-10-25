# -*- coding: utf-8 -*-
import scrapy
from douban_top.items import DoubanTopItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for i in movie_list:
            douban_item = DoubanTopItem()
            #数据解析
            douban_item['serial_number'] = i.xpath(
                ".//div[@class='item']//div[@class='pic']//em/text()").extract_first()
            douban_item['movie_name'] = i.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a//span/text()").extract_first()
            content = i.xpath(".//div[@class='info']//div[@class='bd']//p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star']= i.xpath(".//div[@class='info']//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i.xpath(".//div[@class='info']//div[@class='bd']//div['star']//span[4]/text()").extract_first()
            douban_item['describe'] = i.xpath(".//div[@class='info']//div[@class='bd']//p[@class='quote']//span/text()").extract_first()
            #将数据 yield到pipelines中去
            yield douban_item
        #下一页地址 解析下一页地址
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)