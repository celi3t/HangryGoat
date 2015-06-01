# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from hangrygoat.items import HangrygoatItem
import datetime

class SmittenKitchenSpider(CrawlSpider):
    name = 'smitten_kitchen'
    allowed_domains = ['smittenkitchen.com']
    start_urls = ['http://smittenkitchen.com/']

    rules = (
        Rule(LinkExtractor(allow = '^http://smittenkitchen.com/page/\d+/$')),
        Rule(LinkExtractor(allow = '^http://smittenkitchen.com/blog/\d\d\d\d/\d\d/.*/$'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = HangrygoatItem()
        item['title'] = response.xpath('/html/body/div[@id="page"]//div[@class="post"]/h2/a/text()').extract()
        item['timestamp'] = response.xpath('/html/body/div[@id="page"]//div[@class="post"]/div[@class="date"]/text()').extract()
        # print " >>>" + datetime.datetime.strptime(item['timestamp'].encode('utf-8', 'replace').strip(), "%A, %B %d, %Y").isoformat()
        item['url'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()
        item['raw_content'] = response.xpath('/html/body/div[@id="page"]//div[@class="post"]/div[@class="entry"]').extract()
        return item
