from requests import get
import urllib.parse
from bs4 import BeautifulSoup
import crawler
import cookie_cutter

def make_soup(url, cookies_str):
    cookies = cookie_cutter.make_cookie(cookies_str)
    r = cookie_cutter.cookies_get(url,cookies)
    soup = BeautifulSoup(r, 'html.parser')
    return soup

def get_form(soup):
    form = soup.find(name='form')
    return form

def get_action(form, base_url):
    if 'action' in form.attrs:
        action = form['action']
        abs_action = urllib.parse.urljoin(base_url, action)
        return abs_action
    else:
        return None

def get_form_data(form, payload):
    data = {}
    for inp in form('input'):
        if 'name' in inp.attrs: #do we change all hidden fields as well or only just text
            if 'type' not in inp.attrs or inp['type'] == 'text':
                data[inp['name']] = payload
    for inp in form('textarea'):
        if 'name' in inp.attrs:
            data[inp['name']] = payload
    return data

def inject(url, payload, keyword, cookies):
    soup = make_soup(url, cookies)
    form = get_form(soup)
    if form != None:
        action = get_action(form, url)
        if action != None:
            data = get_form_data(form, payload)
            r = requests.post(action, data=data)
            crawler.crawl(url, payload, keyword, cookies)
        else:
            print("No action parameter found, unable to automatically inject, please try without -i flag")
    
