from lxml import html
import requests
import urllib
import os

# XKCD

EXTENSION = ".jpg" # Download extension for the comic images
FIRST_COMIC_TO_DOWNLOAD = 1
LAST_COMIC_TO_DOWNLOAD = 10

def get_comic(comic_number):
    page = requests.get('http://xkcd.com/' + str(comic_number))
    tree = html.fromstring(page.content)
    comic = tree.xpath('//*[@id="comic"]/img/@src')
    return comic

def download_comic(comic, comic_number):
    if not os.path.exists("comics/"):
        os.makedirs("comics/")
    
    for image_url in comic:
        image_url = "http://" + image_url.strip("//")
        urllib.urlretrieve(
            image_url,
            "comics/" + str(comic_number) + EXTENSION)

for comic_number in range(FIRST_COMIC_TO_DOWNLOAD, LAST_COMIC_TO_DOWNLOAD + 1):
    print "Downloading comic number " + str(comic_number)
    comic = get_comic(comic_number)
    download_comic(comic, comic_number)
    comic_number += 1
    print "Comic number " + str(comic_number) + " DOWNLOADED!"

print "-= ALL COMICS DOWNLOADED =-"


