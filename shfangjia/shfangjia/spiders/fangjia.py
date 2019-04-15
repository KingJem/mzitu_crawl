# -*- coding: utf-8 -*-
import scrapy

from ..items import ShfangjiaItem


class FangjiaSpider(scrapy.Spider):
    name = 'fangjia'
    allowed_domains = ['https://sh.esf.fang.com/']
    start_urls = ['https://sh.esf.fang.com/']

    def parse(self, response):
        search_url = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/ul/li/a/@href').getall()
        for i in search_url:
            url = response.urljoin(i)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url, dont_filter=True)

    def parse_url(self, response):
        detil_lists = response.xpath('//h4[@class]/a/@href').getall()

        for detail_url in detil_lists:
            full_info_url = response.urljoin(detail_url)
            yield scrapy.Request(url=full_info_url, callback=self.parse_detail, dont_filter=True)
        next_page = response.xpath('//div[@id="list_D10_15"]/p[last()-2]/a/@href').get()
        url_next = response.urljoin(next_page)
        yield scrapy.Request(url=url_next, callback=self.parse_url)

    def parse_detail(self, response):
        item = ShfangjiaItem()
        # item['huxing'] = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').get().strip()
        # item['chaoxiang'] = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').getall()[1]
        # item['daxiao'] = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get().strip()
        # item['louceng'] = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get()[1]
        item['danjia'] = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').get().strip()
        # item['zhuangxiu'] = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').getall()[1]
        item['jiage'] = response.xpath('//div[@class="trl-item price_esf  sty1"]/i/text()').get()
        item['diqu'] = response.xpath('//a[@id="kesfsfbxq_C03_07"]/text()').getall()[0].strip()
        item['diqu2'] = response.xpath('//a[@id="kesfsfbxq_C03_08"]/text()').getall()[0].strip()
        # item['hexinmaidian'] = response.xpath('//li[@class="font14 hxmd"]/div[2]/div/text()').getall()
        # item['yezhuxintai'] = response.xpath('//li[@class="font14 yzxt"]/div/text()').getall()
        yield item
