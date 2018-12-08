import requests, bs4, urllib.parse,re

def make_soup(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    return soup

def get_form(soup):
    form = soup.find(name='form')
    return form

def get_action(form, base_url):
    action = form['action']
    # action is reletive url, convert it to absolute url
    abs_action = urllib.parse.urljoin(base_url, action)
    return abs_action

def get_form_data(form, org_code):
    data = {}
    for inp in form('input'):
        # if the value is None, we put the org_code to this field
        if "name" in inp:
            print("ok")
            data[inp['name']] = "test"

    return data

if __name__ == '__main__':
    url = 'http://facebook.com'
    soup = make_soup(url)
    form = get_form(soup)
    action = get_action(form, url)
    data = get_form_data(form, '1634')
    print(data)
    # make request to the action using
    r = requests.post(action, data=data)
