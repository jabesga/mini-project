import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import shutil
import time

base_url = 'http://www.mediavida.com/foro/######'
first_page = 0 
last_page = 100
cookies = dict(auth='######', PHPSESSID='######')

def download_image(image, page, image_number):
    image_name = "page{}_{}.{}".format(page, image_number, image[-3:])
    print("Downloading image: {} in url: {}".format(image_name, image))
    path = 'images/{}'.format(image_name)
    try:
        response = requests.get(image, stream=True, timeout=5)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
    except RequestException:
        print("Error downloading image ^")


for page in range(first_page, last_page + 1):
    url = base_url + '/{}'.format(page)
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_images = soup.find_all('img', { "class" : "lazy" })
    image_number = 0
    for image in all_images:
        download_image(image.get('src'), page, image_number)
        image_number += 1
