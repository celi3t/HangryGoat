import scrapy

class BlogTitleSpider(scrapy.Spider):
    name = "blog_title"
    allowed_domains = ["joythebaker.com"]
    start_urls = [
        "http://joythebaker.com/2015/05/let-it-be-sunday-21/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
