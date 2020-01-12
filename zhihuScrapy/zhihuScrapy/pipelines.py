# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ZhihuscrapyPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_port,mongo_db):
        self.mongo_url = mongo_url # 这里可以在setting中制定数据库和集合
        self.mongo_db = mongo_db
        self.mongo_port = int(mongo_port)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URI'),
            mongo_port = crawler.settings.get('MONGO_PORT'),
            mongo_db = crawler.settings.get('MONGO_DATABASE','items')
        )
    
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host=self.mongo_url,port = self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        # str = json.dumps(dict(item),ensure_ascii=False)+"\n";
        # str = unicode.encode(str,'utf-8');
        self.db['name'].update({'name': item['name']},{'$set': item}, True) 
        return item
        # 这里是mongod 的更新操作,如果查询到了那么就使用第一个参数为查询条件,第二个通过$set指定更新的条件,第三个参数表示如果存在则更新如果不存在则插入