import scrapy
from hangrygoat.items import HangrygoatItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BlogTitleSpider(CrawlSpider):
    name = "blog_title"
    allowed_domains = ["joythebaker.com"]
    start_urls = [
        "http://joythebaker.com/2015/05/let-it-be-sunday-21/"
    ]
    
    rules = [Rule(LinkExtractor())]        


    """
    Note: implement parse_item (instead of parse) because it is a CrawlSpider
    """
    def parse_item(self, response):
        item = HangrygoatItem()
        item['title'] = response.xpath('/html/head/meta[@property="og:title"]/@content').extract()
        item['timestamp'] = response.xpath('//span[@class="posted-on"]/a/time[1]/@datetime').extract()
        item['url'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()
        yield item

        # filename = response.url.split("/")[-2]    
        # with open(filename, 'wb') as f:
        #     f.write(response.body)