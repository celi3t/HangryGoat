# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import json
import scrapy


class HangrygoatItem(scrapy.Item):
    title = scrapy.Field()
    timestamp = scrapy.Field()
    url = scrapy.Field()
    raw_content = scrapy.Field()
    source = scrapy.Field()
    crawl_url = scrapy.Field()



class FoodURLItem(scrapy.Item):
    url = scrapy.Field()
    
    
def writeOnFile(item, fileobject):
    fileobject.write(str(item))

    # fileobject.write('{{{title:' + str(item['title']) +';:;'+
    # 'timestamp:' + str(item['timestamp']) +';:;'+
    # 'url:' + str(item['url']) +';:;'+
    # 'original_url:' + str(item['crawl_url']) +';:;'+
    # 'raw_content:' + str(item['raw_content'])+'}}}')
    

def writeTitlesOnFile(item, fileobject):
    fileobject.write('{{{title:' + str(item['title']) +';:;'+
    'timestamp:' + str(item['timestamp']) +';:;'+
    'crawl_url:' + str(item['crawl_url']) +';:;'+
    'url:' + str(item['url']) +'}}}' + '\n')