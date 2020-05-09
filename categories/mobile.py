import requests
import bs4

parts_sites={'%20':[('paytmmall','https://paytmmall.com/shop/search?q=itemsgohere&from=organic&child_site_id=6&site_id=2&category=72873'),('shopclues','https://www.shopclues.com/search?q=redmi&sc_z=2222&z=0&count=9'),('flipkart','https://www.flipkart.com/search?q=itemsgohere&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'),('snapdeal','https://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty')]
             ,'+':[('croma','https://www.croma.com/phones-wearables/c/1'),('amazon','https://www.amazon.in/s?k=item goes here')]}


# funtion to select the site
def scrape_site(site, part_name, soup):
    '''
        Function to call Parts Scraper for respective Site
        It returns list of Part objects corresponding to the given part name in a respective site
        It takes arguments site name, part name, BeautifulSoup object of site
        '''

    if (site == "paytmmall"):
        site = paytmmall
    elif (site == "flipkart"):
        site = flipkart
    elif (site == "snapdeal"):
        site = snapdeal
    elif (site == "shopclues"):
        site = shopclues
    elif (site == "croma"):
        site = croma
    elif (site == "amazon"):
        site = amazon

    part_list = site(soup, part_name, site)

    return part_list


# functions for each site...
def paytmmall(soup, part_name, site):
    '''
        Function to scrape Part from paytmmall
        It returns a list of Part objects satisfying the part name
        It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
        '''

    items = soup.findAll("div", {"class": "_3WhJ"})
    part_list = []

    for i in items:
        try:

            title = i.a['title']
            price = i.find("div", {"class": "_1kMS"}).span.text
            link = "https://paytmmall.com" + i.a['href']
            img_link = i.find('div', {'class': '_3nWP'}).img['src']
            flag = 0
            for word in part_name.split():
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, img_link, site))

        except:
            continue

    return part_list


def flipkart(soup, part_name, site):
    '''
        Function to scrape Part from flipkart
        It returns a list of Part objects satisfying the part name
        It takes Arguments BeautifulSoup object of amazon.in part search, part name
        '''

    items = soup.findAll("div", {"class": "_1UoZlX"})
    part_list = []

    for i in items:
        try:

            title = i.find("div", {"class": "_3wU53n"}).text
            price = i.find("div", {"class": "_6BWGkk"}).find("div", {"class": "_1vC4OE _2rQ-NK"}).text
            link = "https://www.flipkart.com/" + i.a['href']
            img_link = "https://www.flipkart.com/" + \
                       i.find("div", {"class": "_1OCn9C"}).find("div", {'class': '_3BTv9X'}).img['src']
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, img_link, site))

        except:
            continue

    return part_list


'''def snapdeal(soup, part_name,site):

    #Function to scrape Part from snapdeal
    #It returns a list of Part objects satisfying the part name
    #It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name

    items = soup.findAll("div", {"class": "product-tuple-description"})
    part_list = []
    for i in items:
        try:
            title = i.find('p', {'class': 'product-title'}).text
            price = i.find('span', {'class': 'lfloat product-price'}).text.replace('Rs. ', '₹')
            try:
                img_link = i.find('img', {'class': 'product-image'})['src']
            except:
                img_link = i.find('img', {'class': 'product-image'})['data-src']
            link = i.find('a', {"class": "dp-widget-link noUdLine"})['href']
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, img_link ,site))
        except:
            continue
    return part_list
'''


def shopclues(soup, part_name, site):
    '''
        Function to scrape Part from shopclues
        It returns a list of Part objects satisfying the part name
        It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
        '''

    items = soup.findAll("div", {"class": "column col3 search_blocks"})
    part_list = []

    for i in items:
        try:

            price = i.find("div", {"class": "ori_price"}).find("span", {"class": "p_price"}).text
            title = i.h2.text
            link = i.a['href']
            try:
                img_link = 'https:' + i.find('div', {'class': 'img_section'}).img['src']
            except:
                img_link = 'https:' + i.find('div', {'class': 'img_section'}).img['data-img']
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, img_link, site))

        except:
            continue

    return part_list


def croma(soup, part_name, site):
    '''
        Function to scrape Part from croma
        It returns a list of Part objects satisfying the part name
        It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
        '''

    items = soup.findAll("div", {"class": "row"})
    part_list = []

    for i in items:
        try:

            title = i.find("div", {"class": "row", "style": " margin-right: 0;"}).find("a", {
                "class": "product__list--name"}).h3.text
            link = "https://www.croma.com" + i.find("div", {"class": "row", "style": " margin-right: 0;"}).a['href']
            price = i.find("div", {"class": "row", "style": " margin-right: 0;"}).find("div",
                                                                                       {"class": "_priceRow"}).find(
                "span", {"class": "pdpPrice"}).text
            img_link = i.find('div', {'class': 'col-md-2 col-xs-12 col-sm-3'}).picture.source['data-srcset']
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, site))

        except:
            continue

    return part_list


def amazon(soup, part_name, site):
    '''
        Function to scrape Part from amazon
        It returns a list of Part objects satisfying the part name
        It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
        '''

    items = soup.findAll("div", {"class": "sg-col-inner"})
    part_list = []

    for i in items:
        try:

            title = i.find('a', {"class": "a-link-normal a-text-normal"}).find('span', {
                'class': 'a-size-medium a-color-base a-text-normal'}).text
            price = i.find("div", {"class": "a-row a-size-small"}).find('a', {'class': 'a-link-normal'}).find('span', {
                'class': 'a-size-base'}).text
            link = "https://amazon.in" + \
                   i.find("div", {"class": "a-section a-spacing-none"}).find('a', {'class': 'a-link-normal'})[
                       'href'].strip()
            img_link = i.find("div", {"class": "a-section aok-relative s-image-fixed-height"}).img["src"]
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link, img_link, site))

        except:
            continue

    return part_list