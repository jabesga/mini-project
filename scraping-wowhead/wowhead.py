import requests
from bs4 import BeautifulSoup

FIRST_ITEM = 1
LAST_ITEM = 1000

for item in range(FIRST_ITEM, LAST_ITEM + 1):
    url ='http://www.wowhead.com/item=%s' % str(item)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    if(soup.title.string != 'Error - Wowhead'):
        item_name = soup.title.string.split('- Item - World of Warcraft')[0]
        print(item_name + '| Item number: ' + str(item))