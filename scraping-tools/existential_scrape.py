from lxml import html
import requests
import urllib
import os

# A philosophy webcomic about the inevitable anguish
# of living a brief life in an absurd world. Also Jokes

EXTENSION = ".jpg" # Download extension for the comic images
FIRST_COMIC_TO_DOWNLOAD = 1
LAST_COMIC_TO_DOWNLOAD = 10

def get_comic(comic_number):
    page = requests.get('http://existentialcomics.com/comic/' + str(comic_number))
    tree = html.fromstring(page.content)
    comic = tree.xpath('//*[@id="content"]/img[@class="comicImg"]/@src')
    return comic

def download_comic(comic, comic_number):
    image_number = 0

    if not os.path.exists("comics/" + str(comic_number)):
        os.makedirs("comics/" + str(comic_number))
    
    for image_url in comic:
        print "\tDownloading comic image " + str(image_number)
        urllib.urlretrieve(
            image_url,
            "comics/" + str(comic_number) + "/" + str(image_number) + EXTENSION)
        image_number += 1


for comic_number in range(FIRST_COMIC_TO_DOWNLOAD, LAST_COMIC_TO_DOWNLOAD + 1):
    print "Downloading comic number " + str(comic_number)
    comic = get_comic(comic_number)
    download_comic(comic, comic_number)
    comic_number += 1
    print "Comic number " + str(comic_number) + " DOWNLOADED!"

print "-= ALL COMICS DOWNLOADED =-"


