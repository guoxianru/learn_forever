# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from .settings import MONGD_URI, MONGD_DB


class TianyanchaPipeline_mongodb(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGD_URI)
        self.db = self.client[MONGD_DB]
        self.col = self.db['cha']

    def open_spider(self, spider):
        self.col.create_index([('uuid', pymongo.ASCENDING)], unique=True)

    def process_item(self, item, spider):
        self.col.update({'uuid': item.get('uuid')}, {'$set': item}, True)
        return item

    def close_spider(self, spider):
        self.client.close()
