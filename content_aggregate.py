import requests
from bs4 import BeautifulSoup

urls = {"https://www.amazon.in/s?k=":"+",
"https://www.flipkart.com/search?q=":"%20",
"https://mdcomputers.in/index.php?category_id=0&search=item&submit_search=&route=product%2Fsearch":"+",
"https://www.vedantcomputers.com/index.php?route=product/search&search=":"%20",
"https://www.primeabgb.com/?post_type=product&taxonomy=product_cat&s=":"+"}

headers ={
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
}

def amasearch(item):

    res = requests.get("https://www.amazon.in/s?k="+('+'.join(item.split())), headers = headers)
    soup = BeautifulSoup(res.text, "html.parser")
    result = soup.findAll("span", {"class":"a-size-medium a-color-base a-text-normal"})
    print(result)

def flipsearch(item):
    res = requests.get("https://www.flipkart.com/search?q="+('%20'.join(item.split())), headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")
    result = soup.findAll("div", {"class":"_3wU53n"})
    print(result)

def mdsearch(item):
    res = requests.get("https://mdcomputers.in/index.php?category_id=0&search=item&submit_search=&route=product%2Fsearch".replace("item",('+'.join(item.split()))), headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")
    result = soup.findAll("div", {"class":"right-block right-b"})
    print(result)

def vedsearch(item):
    res = requests.get("https://www.vedantcomputers.com/index.php?route=product/search&search="+('%20'.join(item.split())), headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")
    result = soup.findAll("div",{"class":"product-details"})
    print(result)

def primesearch(item):
    res = requests.get("https://www.primeabgb.com/?post_type=product&taxonomy=product_cat&s="+('+'.join(item.split())), headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")
    result = soup.findAll("div",{"class":"product-innfo"})
    print(result)

primesearch("gtx 1660 super")
