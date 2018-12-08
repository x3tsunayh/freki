# checker.py
#from bs4 import BeautifulSoup
#from requests import get

#TODO: optimise
def checker(soup, payload):
    arrOfLines = str(soup).splitlines()
    for line in arrOfLines:
        if payload in line:
            return True
    return False
    

#test
#response = get("http://192.168.18.133/MCIR/xssmh/challenges/challenge2.php", stream=True)
#soup = BeautifulSoup(response.content, features="html.parser")
#print(checker(soup, "hidden"))
