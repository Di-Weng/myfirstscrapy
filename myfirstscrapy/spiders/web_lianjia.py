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
from myfirstscrapy.items import loupanItem
from scrapy.loader import ItemLoader
import json

global out_dic
out_dic = {}



class Myfirstscrapy(scrapy.Spider):
    name = "web_lianjia_xm"
    allowed_domains = ["xm.lianjia.com"]
    start_urls = [
        "https://xm.lianjia.com/ershoufang/pg1"
    ]

    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }

    for page in range(2,101):
        url = "https://xm.lianjia.com/ershoufang/pg{0}/".format(page)
        start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback = self.parse, cookies={'https://xm.lianjia.com': 'true'}, headers=self.headers)

    def parse(self, response):
        # url_dic = {}
        global out_dic

        ul = response.css("ul.sellListContent")
        for li in ul.css("li.LOGCLICKDATA"):
            item = loupanItem()
            item['title'] = li.css("a[data-el='region']::text").extract()[0]
            # title = li_first.css("h3.name::text").extract()[0]
            item['id'] = li.css("div.title").css("a::attr(data-housecode)").extract()[0]
            item['price'] = li.css("div.unitPrice::attr('data-price')").extract()[0]
            yield item


            # price = house_list.css("span.price_num::text").extract()[0]
            # print(title + ':' +price)

            # with open(r'C:\Users\root\Desktop\house_price.txt', 'a+', encoding='utf-8') as f:
            #     f.write(title)
            #     f.write(',')
            #     f.write(price)
            #     f.write('\n')
            # yield scrapy.Request(response, callback=self.parse_dir_contents, meta=)
        # print(url_dic)
    #
    # def parse_dir_contents(self, response):
    #     print('_____')
    #     print(response.body().decode('utf-8'))
    #     for sel in response.xpath('//ul/li'):
    #         item = MyfirstscrapyItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item