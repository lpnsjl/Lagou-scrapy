# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo


class LagouPipeline(object):
    """def __init__(self):
        self.file = open('lagou.json', 'w')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.file.close()"""

    def __init__(self):
        # mongod的主机号
        host = '127.0.0.1'
        # mongod的端口号
        port = 27017
        # 数据库的名字
        dbname = 'lagou'
        # 表的名字
        sheetname = 'position'
        # 创建一个mongod客户端
        mongoclient = pymongo.MongoClient(host=host, port=port)
        # 创建数据库
        mydb = mongoclient[dbname]
        # 创建表
        self.sheet = mydb[sheetname]

    def process_item(self, item, spider):
        position_info = dict(item)
        # 把数据放入mongod数据库中
        self.sheet.insert(position_info)
        return item
