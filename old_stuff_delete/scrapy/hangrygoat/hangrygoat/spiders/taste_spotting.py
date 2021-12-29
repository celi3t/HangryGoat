# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from hangrygoat.items import HangrygoatItem


class TasteSpottingSpider(CrawlSpider):
    name = 'tastespotting'
    allowed_domains = ['tastespotting.com']
    start_urls = ['http://www.tastespotting.com/',
    'http://www.tastespotting.com/browse/1',
    ]
    
#        #Rule(LinkExtractor(allow = 'http://www.tastespotting.com/browse/\d$')),
    rules = (
        Rule(LinkExtractor(allow = 'http://www.tastespotting.com/$')),
        Rule(LinkExtractor(allow = 'http://www.tastespotting.com/browse/\d+$'), callback='parse_item', follow=True)
    )
    
    def __init__(self, *args, **kwargs):        
        self.outlist = list()
        super(TasteSpottingSpider, self).__init__(*args, **kwargs)
        

    def parse_item(self, response):
        
        filename = 'tastespotting' + '.html'
        with open(filename, 'a') as f:
            res = response.xpath('//span[@class="center-floater"]').extract() #/h3/a/@href
            for item in res:
                if len(item.split('<p>')) > 1:
                    splitem = item.split('<p>')[1].split('</p>')[0].lstrip('www.')
                    if splitem not in self.outlist:
                        self.outlist.append(splitem)
                        f.write(splitem + '\n')#
                else:
                    pass


