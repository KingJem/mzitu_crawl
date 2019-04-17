#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: spider2.py.py
@time: 2019/4/15 23:10
"""

import scrapy

from ..items import ShfangjiaItem


class FangjiaSpider(scrapy.Spider):
    name = 'fangjia2'
    allowed_domains = ['https://sh.esf.fang.com/']
    start_urls = ['https://sh.esf.fang.com/']

    def parse(self, response):
        search_url = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/ul/li/a/@href').getall()
        for i in search_url:
            url = response.urljoin(i)
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_url, dont_filter=True)

    def parse_url(self, response):
        item = ShfangjiaItem()
        blocks = response.xpath('//div[@class="shop_list shop_list_4"]//dl')
        # blocks = response.xpath('.//div//dl')  #  getall() 把页面提取成文字 get是得到一个文字
        for block in blocks:
            item["xiaoqu"] = block.xpath('./dd[1]/p[2]/a/text()').get()
            item["dizhi"] = block.xpath('./dd[1]/p[2]/span/text()').get()
            item["jiage"] = block.xpath('./dd[@class = "price_right"]/span[1]/b/text()').get()
            item["danjia"] = block.xpath('./dd[@class = "price_right"]/span[2]/text()').get()
            yield item

        next_page = response.xpath('//div[@id="list_D10_15"]/p[last()-2]/a/@href').get()
        url_next = response.urljoin(next_page)
        yield scrapy.Request(url=url_next, callback=self.parse_url, dont_filter=True)
