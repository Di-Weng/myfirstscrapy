import scrapy

from myfirstscrapy.items import MyfirstscrapyItem

class Myfirstscrapy(scrapy.Spider):
    name = "csdn_test"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "https://blog.csdn.net/heiyeshuwu/article/details/44117473",
    ]

    def parse(self, response):
        url_dic = {}
        for a_label in response.css("ul.inf_list li.clearfix"):
            url = a_label.css("a::attr('href')").extract()[0]
            title = a_label.css("a::text").extract()[0]
            url_dic[title] = url
            print(title)
            # yield scrapy.Request(url, callback=self.parse_dir_contents)
        print(url_dic)

    def parse_dir_contents(self, response):
        print('_____')
        print(response.body().decode('utf-8'))
        for sel in response.xpath('//ul/li'):
            item = MyfirstscrapyItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item