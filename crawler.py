from requests import session
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
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


def recursive_crawl(url):
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        print(html.prettify())
		"""
        if checker(html, payload):
            ref_vuln.add(url)
		"""
               
        for i in html.find_all('a', href = True):
            href = i['href']
            if href:
                if href[0] == '/':
                    href = url + href
                if href not in href_set:
                    href_set.add(href)
                    href_lst.append(href)

    
    
def main(input_url, input_payload, input_keyword = '', input_nres = 1000, input_user = '', input_pass = ''):
    initial_url = input_url
    payload = input_payload
    keyword = input_keyword
    nresult = input_nres
    username = input_user
    password = input_pass
    
    href_set = set()
    href_vuln = set()
    href_lst = []
    href_set.add(initial_url)
    href_lst.append(initial_url)
    
    while (href_lst and len(href_set) < nresult):
        recursive_crawl(href_lst[0])
        del href_lst[0]
    
    return list(href_vuln)

##main('https://www.owasp.org/index.php/OWASP_Broken_Web_Applications_Project', 'payload', input_keyword = 'owasp')
