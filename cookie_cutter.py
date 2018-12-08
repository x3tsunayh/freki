from contextlib import closing
from requests import get
from requests.exceptions import RequestException

def make_cookie(cookie_str):
    cookies = {}
    if cookie_str[-1] != ';':
        cookie_str += ';'
    while cookie_str:
        equal_idx = cookie_str.find('=')
        key = cookie_str[:equal_idx]
        cookie_str = cookie_str[equal_idx+1:]
        scoln_idx = cookie_str.find(';')
        cookies[key] = cookie_str[:scoln_idx]
        cookie_str = cookie_str[scoln_idx+1:]
    return cookies

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

def log_error(e):
    """
    Prints errors. 
    """
    print(e)
    
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
