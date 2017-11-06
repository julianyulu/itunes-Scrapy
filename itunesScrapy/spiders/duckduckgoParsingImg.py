# -*- coding: utf-8 -*-
import scrapy

class DuckduckgoparsingimgSpider(scrapy.Spider):
    name = 'duckduckgoParsingImg'
    #allowed_domains = ['https://duckduckgo.com/?q=Imagine+Dragons']
    
    suffix = '&iax=images&ia=images'
    prefix = 'https://duckduckgo.com/?q='
    for name in ['einstein', 'newtown']:
        
        start_urls = [prefix + name + suffix]
        def parse(self, response):
            img_src = response.css('.tile--img__img::attr(src)').extract_first()
            yield img_src

            
        
