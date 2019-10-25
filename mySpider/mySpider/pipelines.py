# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 存储数据或者操作
from pymongo import MongoClient


class KdbPipeline(object):
    collection_name = 'NEWS'

    def __init__(self, mongo_host, mongo_port, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    def from_crawler(cls, crawler):
        return cls(
            crawler.setting.get('MONGO_HOST'),
            int(crawler.setting.get('MONGO_PORT')),
            crawler.setting.get('MONGO_DATABASE')
        )

    def process_item(self, item, spider):
        print(item)
        self.collection.insert_one(dict(item))
        return item

    def open_spider(self, spider):
        self.client = MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.database = self.client[self.mongo_db]
        self.collection = self.database[self.collection_name]

    def close_spider(self, spider):
        self.client.close()
