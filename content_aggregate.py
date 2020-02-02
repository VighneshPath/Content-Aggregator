import requests
from bs4 import BeautifulSoup

comp_parts_sites = {
    "%20":[("vedantcomputers","https://www.vedantcomputers.com/index.php?route=product/search&search=")],
    "+":[("amazon","https://www.amazon.in/s?k="),("mdcomputers","https://mdcomputers.in/index.php?category_id=0&search=item&submit_search=&route=product%2Fsearch"),("primeabgb","https://www.primeabgb.com/?post_type=product&taxonomy=product_cat&s=")]
}

headers ={
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
}

class Part():
    '''
    Class to Represent a Part from a given website
    '''
    def __init__(self, title, price, site):
        self.title = title
        self.price = price
        self.site = site

    def get_price(self):
        return float(''.join(self.price[1:].split(",")))

    def __str__(self):
        return (self.title, self.price, self.site)


def get_soup(url):
    '''
    Function to Get BeautifulSoup Object of url Argument.
    '''
    response = requests.get(url, headers = headers)
    if(response.status_code == requests.codes.ok):
        return (BeautifulSoup(response.text,"html.parser"))
    else:
        return


def get_search_url(part_name, url, space_separator):
    '''
    Function to get the Item Search URL of the part searched for
    It returns search url by replacing spaces with corresponding Space separator of the site
    It takes arguments part name, Site url (site name, search url for the site), Space Separator
    '''
    if(url[0] != "mdcomputers"):
        #mdcomputers uses search of unusual format
        search_url = url[1] + space_separator.join(part_name.split(" "))
    else:
        search_url = url[1].replace("item",space_separator.join(part_name.split(" ")))
    return search_url


def site_func(site, part_name, soup):
    '''
    Function to call Parts Scraper for respective Site
    It returns list of Part objects corresponding to the given part name in a respective site
    It takes arguments site name, part name, BeautifulSoup object of site
    '''
    if(site[0] == "mdcomputers"):
        part_list = mdcomp(soup, part_name)
    elif(site[0] == "amazon"):
        part_list = amazon(soup, part_name)
    elif(site[0] == "vedantcomputers"):
        part_list = vedcomp(soup, part_name)
    elif(site[0] == "primeabgb"):
        part_list = primeabgb(soup, part_name)
    return part_list

def mdcomp(soup, part_name):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
    '''
    results = soup.findAll("div", {"class":"right-block right-b"})
    part_list = []
    for item in results:
        try:
            title = item.h4.a.get_text()
            price = item.find("span",{"class":"price-new"}).get_text()
            link = item.h4.a['href']
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append(Part(title,price,link))
        except:
            continue
    return part_list

def amazon(soup, part_name):
    '''
    Function to scrape Part from amazon.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of amazon.in part search, part name
    '''
    results = soup.findAll("div", {"class":"a-section a-spacing-medium"})
    part_list = []
    for item in results:
        try:
            title = item.find("span",{"class":"a-size-medium a-color-base a-text-normal"}).get_text()
            price = item.find("span",{"class":"a-offscreen"}).get_text()
            link ="https://amazon.in"+item.find("a",{"class":"a-link-normal a-text-normal"})['href']
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append(Part(title,price,link))
        except:
            continue
    return part_list

def vedcomp(soup, part_name):
    '''
    Function to scrape Part from vedantcomputers.com
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of vedantcomputers.com part search, part name
    '''
    results = soup.findAll("div",{"class":"product-details"})
    part_list = []
    for item in results:
        try:
            title = item.find("h4",{"class":"name"}).get_text()
            if(item.find("span",{"class":"price-new"}) == None):
                price = item.find("p",{"class":"price"}).get_text().strip()
            else:
                price = item.find("span",{"class":"price-new"}).get_text().strip()
            link = item.find("h4",{"class":"name"}).a['href']
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append(Part(title,price,link))
        except:
            continue
    return part_list

def primeabgb(soup, part_name):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of primeabgb.com part search, part name
    '''
    results = soup.findAll("div",{"class":"product-innfo"})
    part_list = []
    for item in results:
        try:
            title = item.h3.a.get_text()
            try:
                try:
                    price = item.findAll("span",{"class":"woocommerce-Price-amount amount"})[1].get_text()
                except:
                    price = item.find("span",{"class":"woocommerce-Price-amount amount"}).get_text()
            except:
                continue
            link = item.h3.a['href']
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append(Part(title,price,link))
        except:
            continue
    return part_list

def get_part(part):
    '''
    A function to get All the Part details from the respectives websites
    It returns list of all the Part Objects from various websitespython continue
    It takes one argument of part name
    '''
    parts_list = []
    for space_separator,url in comp_parts_sites.items():
        for a_site in url:
            search_url = get_search_url(part, a_site, space_separator)
            url_soup = get_soup(search_url)
            site_part_list = site_func(a_site, part, url_soup)
            parts_list.extend(site_part_list)
    return parts_list

def sort_according_to_price(part_list):
    '''
    Function to sort The part list according to Price
    It returns a list of Part Objects sorted ascendingly accordingly to their price
    It takes one argument of Unsorted list of Part Objects
    '''
    price_sort = []
    for item in part_list:
        price_sort.append((item.get_price()))
    price_sort.sort()
    new_part_list = []
    for price in price_sort:
        for item in part_list:
            if(item.get_price() == price):
                new_part_list.append(part_list.pop(part_list.index(item)))
    return new_part_list


if __name__ == '__main__':
    print("Enter Part Name")
    part_name = input()
    part_list = get_part(part_name)
    part_list = sort_according_to_price(part_list)
    for part in part_list:
        print(part.title, part.price, part.site)
