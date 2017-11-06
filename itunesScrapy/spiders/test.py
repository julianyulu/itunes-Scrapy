# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    #allowed_domains = ['www.duckduckgo.com']
    #start_urls = ['http://www.duckduckgo.com/']
    suffix = '&iax=images&ia=images'
    prefix = 'https://duckduckgo.com/?q='
    name = 'einstein'
    start_urls = [prefix + name + suffix]
    
    def parse(self, response):
        img_src = response.css('.tile--img__img::attr(src)').extract_first()
        yield img_src
        

    
