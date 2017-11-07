SPIDERS := itunes_song itunes_artist itunes_album

list-spiders:
	scrapy list

check:
	@for i in $(SPIDERS);\
	do \
	echo ;\
	echo "Checking spider $$i";\
	scrapy check $$i;\
	done;

artist:
	@rm itunes_artists.json
	scrapy crawl itunes_artist -o itunes_artists.json
song:
	@rm itunes_songs.json
	scrapy crawl itunes_song -o itunes_songs.json
album:
	@rm itunes_album.json
	scrapy crawl itunes_album -o itunes_album.json

all:
	@for i in $(SPIDERS); \
	do \
	scrapy crawl $$i -o  "$$i""s.json";\
	done;
clean:
	rm *.json
	rm *~
	rm ./itunesScrapy/spiders/*~


