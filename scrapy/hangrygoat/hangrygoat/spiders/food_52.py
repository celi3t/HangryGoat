# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from hangrygoat.items import HangrygoatItem, writeOnFile, writeTitlesOnFile
import datetime


class Food52Spider(CrawlSpider):
    name = 'food_52'
    allowed_domains = ['http://food52.com', 'food52.com', 'https://food52.com']
    start_urls = ['http://food52.com/recipes']

    rules = (
        Rule(LinkExtractor(allow = 'http://food52.com/recipes/\d+-[a-zA-Z0-9\-]'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow = 'http://food52.com/recipes')),
        Rule(LinkExtractor(allow = 'http://food52.com/recipes?page=\d+'))
    )

    def parse_item(self, response):
        
        recipe_item = HangrygoatItem()
        recipe_item['title'] = response.xpath('//header/h1[@class="article-header-title"]/text()').extract()
        recipe_item['timestamp'] = response.xpath('//meta[@created_date]/@created_date').extract()
        recipe_item['url'] = response.xpath('/html/head/meta[@property="og:url"]/@content').extract()
        recipe_item['raw_content'] = response.xpath('//li[@itemprop="recipeInstructions"]/text()').extract()
        recipe_item['source'] = self.name
        recipe_item['crawl_url'] = response.url

        filename = './'+ 'food_522' +'.json'
        with open(filename, 'a') as f:
            writeOnFile(recipe_item, f)
            
        filename = './'+ 'food_52_titles' +'.csv'
        with open(filename, 'a') as f:
            writeTitlesOnFile(recipe_item, f)
        
        yield recipe_item
