from requests import session
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import checker


def cookies_get(url, cookies):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream = True, cookies = cookies)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    Prints errors. 
    """
    print(e)
	
def sanitize_url(url, path):
    if 'http' in path or 'www.' in path:
        return path
    
    if url[-1] == '/':
        url = url[:-1]
    
    if path[0:1] == '/':
        return url + path
    elif path[0:2] == './':
        return url + path[1:]
    elif path[0:3] == '../':
        last_idx = url.rfind('/')
        isFile = url.rfind('.') > last_idx
        if isFile:
            last_idx = url[:last_idx].rfind('/')
        return sanitize_url(url[:last_idx], path[3:])
    else:
        return url + '/' + path


def iter_crawl(url, cookies, keyword, payload, href_vuln, href_set, href_lst):
    response = cookies_get(url, cookies)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        if checker.check(html, payload):
            href_vuln.add(url)
        for i in html.find_all('a', href = True):
            href = i['href']
            if href:
                href = sanitize_url(url, href)
                if href not in href_set and keyword in href:
                    href_set.add(href)
                    href_lst.append(href)

    
    
def crawl(input_url, input_payload, input_keyword, input_cookies, input_nres = 2):
    initial_url = input_url
    payload = input_payload
    keyword = input_keyword
    nresult = input_nres
    
    cookies = {}
    cookie_str = input_cookies
    if cookie_str[-1] != ';':
        cookie_str += ';'
    while cookie_str:
        equal_idx = cookie_str.find('=')
        key = cookie_str[:equal_idx]
        cookie_str = cookie_str[equal_idx+1:]
        scoln_idx = cookie_str.find(';')
        cookies[key] = cookie_str[:scoln_idx]
        cookie_str = cookie_str[scoln_idx+1:]  
    print(cookies)
    
    href_set = set()
    href_vuln = set()
    href_lst = []
    href_set.add(initial_url)
    href_lst.append(initial_url)
    
    while (href_lst and len(href_set) < nresult):
        iter_crawl(href_lst[0], cookies, keyword, payload, href_vuln, href_set, href_lst)
        del href_lst[0]
    
    if not href_vuln:
        print("No persistent XSS found on crawled sites.")
    else:
        print("Persistent XSS found on these sites:")
        for i in href_vuln:
            print(i)

#crawl('https://stackoverflow.com/questions/7253803/how-to-get-everything-after-last-slash-in-a-url', 'rstrip', input_keyword = 'python', input_cookies = '')
