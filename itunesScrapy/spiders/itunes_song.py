# -*- coding: utf-8 -*-
import scrapy


class ItunesSongSpider(scrapy.Spider):
    name = 'itunes_song'
    #allowed_domains = ['https://www.apple.com/itunes/charts/songs/']
    start_urls = ['https://www.apple.com/itunes/charts/songs/']
    songs_exist = []
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
            if item[0] in self.songs_exist:
                pass
            else:
                self.songs_exist.append(item[0])
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
