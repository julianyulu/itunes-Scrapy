# -*- coding: utf-8 -*-
import scrapy


class ItunesArtistSpider(scrapy.Spider):
    name = 'itunes_artist'
    #allowed_domains = ['https://www.apple.com/itunes/charts/songs/']
    start_urls = ['https://www.apple.com/itunes/charts/songs/']
    artists_exist = []
    DOWNLOAD_DELAY = 0.1
    def parse(self, response):
        artist = response.css('h4 a::text').extract()
        artist_link = response.css('h4 a::attr(href)').extract()
        
        for arti, arti_link in zip(artist, artist_link):
            if arti in self.artists_exist:
                pass
            else:
                self.artists_exist.append(arti)
                request = scrapy.Request(arti_link, callback=self.parse_artistLink)
                request.meta['artist'] = arti
                yield request
    
    def parse_artistLink(self, response):
        artist = response.meta['artist']
        artist_link = response.url
        origin = response.css('.bordered-list__subtitle::text').extract_first().strip()
        genre = response.css('a.link div::text').extract_first().strip()
        born = response.css('.bordered-list__copy dd::text').extract()[-1].strip()
        intro = ''.join(response.css('.we-about-artist-inline__desc--detailed ::text').extract()).strip()
        latest_release =  response.css('h3.we-lockup__title::text').extract_first()

        
        artist_pic_link = response.css('.we-artwork--background-image style').re_first(r'url\(([^\)]+)') # background image from <style>
        if type(artist_pic_link) == str:
            pass
        else:
            artist_pic_link = response.css('.we-about-artist-inline__artwork-link .we-artwork__image::attr(src)').extract_first() # html image
        
        scraped_info = {
            'artist': artist,
            'artist_link': artist_link,
            'artist_pic_link': artist_pic_link,
            'origin': origin,
            'genre': genre,
            'born': born,
            'latest_release': latest_release,
            'intro': intro
            }
        yield scraped_info

            
            
        
