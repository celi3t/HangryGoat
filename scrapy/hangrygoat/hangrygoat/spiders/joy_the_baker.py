import scrapy
from hangrygoat.items import HangrygoatItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class JoyTheBakerSpider(CrawlSpider):
    name = "joy_the_baker"
    allowed_domains = ["joythebaker.com"]
    start_urls = [
        "http://joythebaker.com/"
    ]

    rules = [
        Rule(LinkExtractor(allow = '^http://joythebaker.com/page/\d+/$')),
        Rule(LinkExtractor(allow = '^http://joythebaker.com/\d\d\d\d/\d\d/.*/$'), callback='parse_item', follow=True)
    ]


    """
    Note: implement parse_item (instead of parse) because it is a CrawlSpider
    """
    def parse_item(self, response):
        item = HangrygoatItem()
        item['title'] = response.xpath('/html/head/meta[@property="og:title"]/@content').extract()
        item['timestamp'] = response.xpath('//span[@class="posted-on"]/a/time[1]/@datetime').extract()
        item['url'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()
        item['raw_content'] = response.xpath('//div[@class="entry-content"]/*[not(self::div)]/text()').extract()
        item['source'] = self.name
        item['crawl_url'] = response.url
        yield item
