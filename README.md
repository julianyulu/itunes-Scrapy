# iTunes-Scrapy
Auto scrape daily top rated songs, artists, albums from itunes  
data save scraped data in .json file.

## Spiders  
+ itunes_song
+ itunes_artist
+ itunes_album

## Structure  
```
scrapy.cfg
requirements.txt
makefile
itunesScrapy/
	__init__.py
	items.py
	piplines.py
	settings.py
	spiders/
		__init__.py
		itunes_song.py
		itunes_artist.py
		itunes_album.py
```

## How to run  
Clone this repository:  
```
git clone git@github.com:SuperYuLu/itunes-Scrapy.git
```
Install dependencies:  
```
pip install -r requirements.txt
```
List spiders:  
```
make list-spiders
```
Check spiders:  
```
make check
```
Run all spiders:  
```
make clean
make all
```
Run single spider:  
```
make song (or artist or album)
```
Clean meta files and output json files:  
```
make clean
```

## Output Files  
+ itunes_songs.json
+ itunes_artists.json
+ itunes_albums.json  
Check example output in folder *examples*  


