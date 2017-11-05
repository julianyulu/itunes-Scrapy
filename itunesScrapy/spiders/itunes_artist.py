# -*- coding: utf-8 -*-
import scrapy


class ItunesArtistSpider(scrapy.Spider):
    name = 'itunes_artist'
    #allowed_domains = ['https://www.apple.com/itunes/charts/songs/']
    start_urls = ['https://www.apple.com/itunes/charts/songs/']

    def parse(self, response):
        artist = response.css('h4 a::text').extract()
        artist_link = response.css('h4 a::attr(href)').extract()
        for arti, arti_link in zip(artist, artist_link):
            request = scrapy.Request(arti_link, callback=self.parse_artistLink)
            request.meta['artist'] = artist
            yield Request

    def parse_artistLink(self, response):
        artist = response.meta['artist']
        artist_link = response.url
        
