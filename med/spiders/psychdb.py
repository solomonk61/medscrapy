import scrapy


class PsychdbSpider(scrapy.Spider):
    name = 'psychdb'
    allowed_domains = ['psychdb.com']
    start_urls = ['http://psychdb.com/']

    def parse(self, response):
        pass
