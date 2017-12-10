# -*- coding: utf-8 -*-
import scrapy


class ItunesAlbumSpider(scrapy.Spider):
    name = 'itunes_album'
    #allowed_domains = ['https://www.apple.com/itunes/charts/songs/']
    start_urls = ['https://www.apple.com/itunes/charts/songs/']
    albums_exist = []
    DOWNLOAD_DELAY = 0.1
    def parse(self, response):
        artist = response.css('h4 a::text').extract()
        album_link = response.css('li h3 a::attr(href)').extract()
        
        for arti, link in zip(artist, album_link):
            if link in self.albums_exist:
                pass
            else:
                self.albums_exist.append(link)
                request = scrapy.Request(link, callback = self.parse_albumLink)
                request.meta['artist'] = arti
                yield request
    
    def parse_albumLink(self, response):
        album = response.css('.t-hero-headline::text').extract_first()
        album_link = response.url
        album_img_link = response.css('.product-artwork img.we-artwork__image::attr(src)').extract_first()
        release_time = response.css('.inline-list__item--bulleted time ::text').extract_first(default='N/A')
        artist = response.meta['artist']
        genre = response.css('.inline-list__item a::text').extract_first()
        intro = response.css('.product-hero-desc__section p::attr(aria-label)').extract_first()
        num_of_songs = response.css('.product-artwork-caption p::text').re_first('\d+')

        # Track table
        track_num = response.css('.table__row__number::text').re('\d+')
        track_name_temp = response.css('.t-table-headline::text').extract()
        track_name = [x.strip() for x in track_name_temp]
        track_time = response.css('.table__row__duration::text').extract()
        track = list(zip(track_num, track_name, track_time))

        scraped_info = {
            'album': album,
            'album_link': album_link,
            'album_img_link': album_img_link,
            'release_time': release_time,
            'intro': intro,
            'artist': artist,
            'genre': genre,
            'num_of_songs': num_of_songs,
            'track': track
            }
        yield scraped_info


        
        
           
