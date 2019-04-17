# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ShfangjiaPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect('localhost', 'root', 'root', 'test')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据

        # self.cursor.execute( "insert into sh(huxing,changxiang,daxiao,louceng,danjia,zhuangxiu,jiage,diqu,diqu2,) VALUES ('{},{},{},{},{},{},{},{},{},{},{}')".format(
        #         item['huxing'], item['chaoxiang'], item['daxiao'], item['louceng'], item['danjia'], item['zhuangxiu'],
        #         item['jiage'], item['diqu'],item['diqu2']))
        # sql = "insert into fangjia(DIQU,DIQU2,DANJIA,JIAGE) values('%s','%s','%s')"%( item["diqu"], item["diqu2"], item["jiage"])
        # sql = "insert into fangjia(id,danjia,diqu,diqu2,jiage) values(null,item['danjia'],item['diqu'],item['diqu2'],item['jiage'])"
        sql = """insert into fangjia(id,xiaoqu,dizhi,danjia,jiage) values(null,%s,%s,%s,%s)"""
        self.cursor.execute(sql, (item['xiaoqu'], item['dizhi'], item['danjia'], item['jiage']))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

# import scrapy
# from scrapy import signals
# import json, codecs
#
#
# class ShfangjiaPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class JsonWithEncodingShfangjiaPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('fanjia.json', 'a', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + '\n\n'
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()
#
#
#
#
# import pymysql
#
#
# class ShfangjiaPipeline(object):
#     def __int__(self):
#         dbparama = {
#             "host": "127.0.0.1",
#             "port": 3306,
#             "user": "root",
#             "password": "root",
#             "database": "sh_test",
#             "char_set": "utf8"
#         }
#         self.conn = pymysql.connect(**dbparama)
#         self.cursor = self.conn.cursor()
#         self.sql = """
#                     INSERT INTO fangjia(id,diqu,diqu2,danjia,jiage) VALUES (NULL,%s,%s,%s,%s)
#                     """
#
#         def process_item(self, item, spider):
#             self.cursor.execute(self.sql, item["diqu"], item["diqu2"], item["danjia"], item["jiage"])
#             self.conn.commit()
#             return item
