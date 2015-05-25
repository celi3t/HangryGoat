import scrapy
from hangrygoat.items import HangrygoatItem

class BlogTitleSpider(scrapy.Spider):
    name = "blog_title"
    allowed_domains = ["joythebaker.com"]
    start_urls = [
        "http://joythebaker.com/2015/05/let-it-be-sunday-21/"
    ]

    def parse(self, response):
        item = HangrygoatItem()
        item['title'] = response.xpath('/html/head/meta[@property="og:title"]/@content').extract()
        item['timestamp'] = response.xpath('//span[@class="posted-on"]/a/time[1]/@datetime').extract()
        item['url'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()
        yield item
