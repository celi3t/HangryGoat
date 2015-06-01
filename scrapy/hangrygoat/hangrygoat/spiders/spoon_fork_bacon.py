# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from hangrygoat.items import HangrygoatItem


class SpoonForkBaconSpider(CrawlSpider):
    name = 'spoon_fork_bacon'
    allowed_domains = ['spoonforkbacon.com']
    start_urls = ['http://www.spoonforkbacon.com/']

    rules = (
        Rule(LinkExtractor(allow = '^http://www.spoonforkbacon.com/page/\d+/$')),
        Rule(LinkExtractor(allow = '^http://www.spoonforkbacon.com/\d\d\d\d/\d\d/.*/$'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = HangrygoatItem()
        item['title'] = response.xpath('/html/body//h1[@class="entry-title"]/a/span/text()').extract()
        item['timestamp'] = response.xpath('/html/head/meta[@property="article:published_time"]/@content').extract()
        item['url'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()
        item['raw_content'] = response.xpath('/html/body//div[@id="blog_content_container"]').extract()
        item['source'] = self.name
        item['crawl_url'] = response.url
        return item
