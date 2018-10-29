# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from mySpider import settings

class MyspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DB,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWORD
            # charset = 'utf-8'
            # use_unicode = True
        )
        self.cursor  = self.connect.cursor()
    def process_item(self, item, spider):
        try:
            print(item["name"],"********************")
            self.cursor.execute("insert into urlinfo(url,name) values(%s,%s)",("ass","rtt"))
            # print(self.cursor.fetchone())
            print(len(item["url"]),len(item["name"]))
            for i in range(min(len(item["url"]),len(item["name"]))):

                self.cursor.execute("""
                insert into urlinfo(url,name) values (%s,%s)
                """,(
                   item["url"][i],
                    item["name"][i]
                ))

            self.connect.commit()
        except Exception as er:
            print("*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(er)
        return item
