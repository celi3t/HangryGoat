# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

from hangrygoat.items import HangrygoatItem


admitted_list = list()
for line in open('/Users/celi/Desktop/FoodMath/hangry-goat.git/scrapy/hangrygoat/hangrygoat/spiders/tastespotting.csv', 'r'):
    admitted_list.append(line.rstrip())
# admitted_list.append('smittenkitchen.com')
# admitted_list.append('shutterbean.com')
# admitted_list.append('joythebaker.com')
# 
# admitted_list = set(admitted_list)
# admitted_list = list(admitted_list)
# 
# admitted_list = list()
# # for line in open('/spiders/tastespotting.html', 'r'):
# #     admitted_list.append(line.rstrip())
# admitted_list.append('smittenkitchen.com')
# admitted_list.append('shutterbean.com')
# admitted_list.append('joythebaker.com')
# 
# admitted_list = set(admitted_list)
# admitted_list = list(admitted_list)


class GeneralSpider(CrawlSpider):
    name = 'linkfinder'

    def __init__(self, starturl=None, max_pages = 1000, *args, **kwargs):
        
        self.start_urls = ['http://www.' + starturl + '/', 'http://' + starturl + '/']
        self.allowed_domains = [starturl]
        self.max_pages = max_pages
        self.page_counter = 0
        
        self.rules = (
        Rule(LinkExtractor(allow = '^http://' + 'www.' + self.allowed_domains[0] + '/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow = '^http://' + self.allowed_domains[0] + '/'), callback='parse_item', follow=True)
        )
        
        super(GeneralSpider, self).__init__(starturl, *args, **kwargs)
            


    def parse_item(self, response):
        
    
            
        matched_file = open('./matches.csv', 'a')     
        links = response.xpath('/html//a/@href').extract()
        
        for link in links:
            slink = link.split('/')
            if len(slink) > 2:
                #print slink[2].lstrip('www.')
                if slink[2].lstrip('www.') in admitted_list:
                    if slink[2].lstrip('www.') != self.allowed_domains[0]:
                        print 'match found!', self.allowed_domains[0], slink[2].lstrip('www.')
                        matched_file.write(self.allowed_domains[0] + ',' + slink[2].lstrip('www.') + '\n')
        self.page_counter += 1
        if self.page_counter > self.max_pages:
            raise CloseSpider('MaxN pages scraped reached')
                        
                        

