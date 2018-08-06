import scrapy

from myfirstscrapy.items import MyfirstscrapyItem

class Myfirstscrapy(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "https://blog.csdn.net/heiyeshuwu/article/details/44117473",
    ]

    def parse(self, response):
        url_list = []
        for href in response.css("ul.inf_list > li.clearfix > a::attr('href')"):
            url = href.extract()
            url_list.append(href)
            # yield scrapy.Request(url, callback=self.parse_dir_contents)
        print('@@@@@@@@@@@@@@')
        print(url_list)

    def parse_dir_contents(self, response):
        print('_____')
        print(response.body().decode('utf-8'))
        for sel in response.xpath('//ul/li'):
            item = MyfirstscrapyItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item