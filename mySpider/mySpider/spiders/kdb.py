# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from mySpider.items import Kdb
from urllib.request import urlopen


class KdbSpider(scrapy.Spider):
    name = 'kdb'
    # allowed_domains = ['news.163.com/']
    start_urls = ['https://news.163.com/']
    custom_settings = {
        # 'LOG_LEVEL': 'ERROR'
        # 定义错误级别过滤掉scrapy一些系统级别的错
    }

    def parse(self, response):
        bs = BeautifulSoup(response.body, 'html.parser')
        urls = bs.find_all('a', href=re.compile("(http|https):\/\/\w+\.\d+\.com\/\d{2}\/(\w|\d|\/|\.)*"), string=True)
        for url in urls:
            link = url.get('href')
            text = url.text.strip()  # 可以将前后的空格去掉
            # yield是进一步处理的意思
            yield scrapy.Request(link, callback=self.parse_details)

    def parse_details(self, response):
        # 注意中文乱码
        bs = BeautifulSoup(response.body, 'html.parser', from_encoding="gb18030")
        try:
            title = self.extract_title(bs)
            if title is None:
                raise Exception('title_not_found for ' + response.url.strip())
            pub_data = self.extract_pub_date(bs)
            if pub_data is None:
                raise Exception('pub_data_not found for ' + response.url.strip())

            content = self.extract_content(bs)
            if content is None:
                raise Exception('content_not_found ' + response.url.strip())
            item = Kdb(_id=response.url, title=title, pub_data=pub_data)
            yield item
        except Exception as e:
            self.logger.error(str(e))

    def extract_title(self, bs):
        selectors = [".bannertext h1", ".post_content_main h1", ".brief h1", ".left h1"]
        for selector in selectors:
            if len(bs.select(selector)) != 0:
                title = bs.select(selector)[0].get_text()
                return title

    def extract_pub_date(self, bs):
        selectors = [".post_time_source", ".pub_time", "#ptime"]
        for selector in selectors:
            if len(bs.select(selector)) != 0:
                if selector == '.post_time_source':
                    news_time = bs.select(selector)[0].get_text()
                    news_time = re.findall("\d{4}-\d{2}-\d{2}\s\d+:\d+:\d+", news_time.strip())
                    return news_time
                else:
                    return bs.select(selector)[0].get_text()

    def extract_content(self, bs):
        selectors = ["div#endText p"]
        for selector in selectors:
            if len(bs.select(selector)) != 0:
                content = '\n'.join([p.text for p in bs.select(selector)])
                return content
