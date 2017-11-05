# -*- coding: utf-8 -*-
import scrapy


class ItunesbotSpider(scrapy.Spider):
    name = 'itunesbot'
    #allowed_domains = ['https://www.apple.com/itunes/charts/songs/']
    start_urls = ['https://www.apple.com/itunes/charts/songs/']
    def parse(self, response):
        
        song = response.css('h3 a::text').extract()
        artist = response.css('h4 a::text').extract()
        rank = response.css('li strong::text').extract()
        albumLink = response.css('li h3 a::attr(href)').extract()
                
        for item in zip(song, artist, rank, albumLink):
            scraped_info = {
                'song': item[0],
                'artist': item[1],
                'rank': item[2],
                'albumLink': item[3]
                }
            request = scrapy.Request(item[3], callback=self.parse_albumLink)
            request.meta['scraped_info'] = scraped_info
            yield request
            
        
    def parse_albumLink(self, response):
        scraped_info = response.meta['scraped_info']
        album = response.css('.t-hero-headline::text').extract_first()
        genre = response.css('.inline-list__item a::text').extract_first()
        duration = response.css('.is-active .table__row__duration::text').extract_first()
        release_time = response.css('.inline-list__item--bulleted time ::text').extract_first(default='N/A')
        
        scraped_info['album'] = album
        scraped_info['duration'] = duration
        scraped_info['genre'] = genre
        scraped_info['release_time'] = release_time
        yield scraped_info
