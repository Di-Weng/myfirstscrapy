#!/usr/bin/env python

# _*_ coding:utf-8 _*_

'''

@author: diw

@contact: di.W@hotmail.com

@file: xmhouse.py

@time: 2018/8/7 23:10

@desc:

'''

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
import re

global out_dic
out_dic = {}



class Myfirstscrapy(scrapy.Spider):
    name = "xmhouse"
    allowed_domains = ["esf.xmhouse.com"]
    start_urls = [
        "http://esf.xmhouse.com/sell/t_r3502030000_a_u_l_z_s1_itp_b_it_if_ih_p-_ar-_pt_o0_psundefined_1.html?keyWord="
    ]

    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }
# 744
    for page in range(2,3):
        url = "http://esf.xmhouse.com/sell/t_r3502030000_a_u_l_z_s1_itp_b_it_if_ih_p-_ar-_pt_o0_psundefined_{0}.html?keyWord=".format(page)
        start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback = self.parse, cookies={'http://esf.xmhouse.com/': 'true'}, headers=self.headers)

    def parse(self, response):
        print('aa')
        info_div = response.css("div.listHavePic")
        print(info_div)
        for house_div in info_div.css("dl"):
            title = house_div.css("dd.detail").css("span.xuzhentian").css("a::text").extract()[0]
            price_info_list = house_div.css("dd.detail::text").extract()
            price = 0
            for price_info in price_info_list:
                if(len(price_info.strip())>0):
                    price = re.findall('，.*',price_info)[0].strip().split('，')[-1]
                    break
            item = loupanItem()
            item['title'] = title
            item['price'] = price
            yield item


