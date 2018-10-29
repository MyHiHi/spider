# -*- coding: utf-8 -*-
import scrapy,codecs
from mySpider.items import Info

class SousouSpider(scrapy.Spider):
    name = 'sousou'
    allowed_domains = ['https://yz.chsi.com.cn']
    start_urls =  ['https://yz.chsi.com.cn/kyzx/zcdh/?start='+str(x) for x in range(20,160,40)]
    # start_urls = ['https://yz.chsi.com.cn/kyzx/zcdh/?start=200','https://yz.chsi.com.cn/kyzx/zcdh/?start=80']

    def parse(self, response):
        url = response.xpath("/html/body/div[1]/div[2]/div[3]/div[1]/ul/li/a/@href").extract()
        name = response.xpath("/html/body/div[1]/div[2]/div[3]/div[1]/ul/li/a/text()").extract()
        item = Info()
        item["url"]  = url
        item["name"] = name
        return item

        # with open("test.txt","a") as f:
        #     for i in res:
        #         f.write('https://yz.chsi.com.cn/'+i+"\n")



