import requests
from bs4 import BeautifulSoup

url = '/'


global_list = []
visited_list = []
exclusion_list = ['wp-login', '/wp-content/uploads/']
def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        all_links = soup.find_all('a')
        for link in all_links:
            next_url = link.get('href')
            if next_url not in global_list and '#####' in next_url and not any(exclusion in next_url for exclusion in exclusion_list):
                global_list.append(next_url)
                f = open('links.txt', 'a')
                f.write('{}\n'.format(next_url))
                f.close()

        for link in all_links:
            next_url = link.get('href')
            if next_url not in visited_list and '#####' in next_url and not any(exclusion in next_url for exclusion in exclusion_list):
                visited_list.append(next_url)
                print('Visiting: {}'.format(next_url))
                get_all_links(next_url);
    except requests.exceptions.RequestException:
        print('\tException with URL: {}'.format(url))



get_all_links(url)
