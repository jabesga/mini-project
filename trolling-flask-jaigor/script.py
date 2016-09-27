import requests
from bs4 import BeautifulSoup

session_cookie = dict(session='.eJwlj0uqAjEQAO-StYsk_Um3lxnSn6AICjO6ery7O-CmdgVVf2Vbex63cn3vn7yU7R7lWhLAlPrQcFYF5HDoGokxsNkkjZWWTHpycqugLZB7Y2_cukqEy6iMywiBkyfKJIvhMBEmgXtKoOlQIXTqyoJ9wRSKXi2jXIof-9rer0c-zx5YKi4VvSVpdWGyXh2WZYclEGeTDl5yep8j998Elv8vmxU-8g.CpN1Hw.qZhDw8QXxfMTNKNbLPR3LjxTi8Y')
index_url = 'http://flask-website-example.herokuapp.com/index'
index_response = requests.get(index_url, cookies=session_cookie)

soup = BeautifulSoup(index_response.content, 'html.parser')

def post_on_jaigor_page(text):
    csrf = soup.find('input',{'id':'csrf_token'})['value']
    post_response = requests.post(index_url, cookies=session_cookie, data={'post':text, 'csrf_token': csrf})
    if post_response.status_code == 200:
        pass

# =====================================================
wiki_domain = 'https://en.wikipedia.org'
starting_wiki_url = 'https://en.wikipedia.org/wiki/Diaphragm_(optics)'
def get_a(url):
    wiki_response = requests.get(url)
    wiki_soup = BeautifulSoup(wiki_response.content, 'html.parser')
    a = wiki_soup.find_all('div', {'id':'mw-content-text'})[0].find_all('p')[0].find_all('a')

    i = 0
    a_to_be_returned = a[i]
    while a_to_be_returned['href'].startswith('#'):
        i += 1
        a_to_be_returned = a[i]
    return a_to_be_returned

new_url = starting_wiki_url
limit = 100
for i in range(limit):
    a = get_a(new_url)
    print('Posting about {}'.format(a['title']))
    post_on_jaigor_page(a['title'])
    new_url = wiki_domain + a['href']
