# -*- coding: utf-8 -*-
import pymongo
#引入配置文件
from douban_top.settings import mongo_port,mongo_db_collection,mongo_db_name,mongo_host
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanTopPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname =mongo_db_collection
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
