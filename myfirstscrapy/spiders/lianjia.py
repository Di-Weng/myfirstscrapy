#!/usr/bin/env python

# _*_ coding:utf-8 _*_

'''

@author: diw

@contact: di.W@hotmail.com

@file: lianjia.py

@time: 2018/8/6 23:31

@desc:

'''
import scrapy
from scrapy import settings
from scrapy.http.request import Request
from myfirstscrapy.items import MyfirstscrapyItem

class Myfirstscrapy(scrapy.Spider):
    name = "lianjia_xm"
    allowed_domains = ["m.lianjia.com"]
    start_urls = [
        "https://m.lianjia.com/xm/loupan/pg1"
    ]

    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }

    for page in range(2,4):
        url = "https://m.lianjia.com/xm/loupan/pg{0}/".format(page)
        start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback = self.parse, cookies={'https://m.lianjia.com': 'true'}, headers=self.headers)

    def parse(self, response):
        # url_dic = {}
        print(response)
        district_list = ['思明', '同安', '翔安', '集美', '湖里', '海沧']
        for li_first in response.css("li.resblock-list-item"):
            district = li_first.css("div.resblock-location-line::attr('text')").extract()[0].split('-')[0]
            if(district not in district_list):
                continue
            title = li_first.css("li::attr('data-index')").extract()[0]
            # title = li_first.css("h3.name::text").extract()[0]
            id = li_first.css("li::attr('data-ulog-exposure')").extract()[0].split('=')[-1]
            price = li_first.css("span.price_num").extract()[0]
            print(title)
            # yield scrapy.Request(url, callback=self.parse_dir_contents)
        # print(url_dic)

    def parse_dir_contents(self, response):
        print('_____')
        print(response.body().decode('utf-8'))
        for sel in response.xpath('//ul/li'):
            item = MyfirstscrapyItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item