import requests
import bs4

parts_sites={'%20':[('www.paytmmall.com','https://paytmmall.com/shop/search?q=item goes here'),('www.flipkart.com','https://www.flipkart.com/search?q=item goes here'),('www.shopclues.com','https://www.shopclues.com/search?q=item goes here'),]
             ,'+':[('www.croma.com','https://www.croma.com/search/?text=item goes here'),('www.amazon.in','https://www.amazon.in/s?k=item goes here')]}
# in %20 : ('www.snapdeal.com','https://www.snapdeal.com/search?keyword=items goes here')

# funtion to select the site
def scrape_site(site, part_name, soup):
    '''
        Function to call Parts Scraper for respective Site
        It returns list of Part objects corresponding to the given part name in a respective site
        It takes arguments site name, part name, BeautifulSoup object of site
        '''

    if (site == "www.paytmmall.com"):
        site_function = paytmmall
    elif (site == "www.flipkart.com"):
        site_function = flipkart
    #elif (site == "www.snapdeal.com"):
    #    site_function = snapdeal
    elif (site == "www.shopclues.com"):
        site_function = shopclues
    elif (site == "www.croma.com"):
        site_function = croma
    elif (site == "www.amazon.in"):
        site_function = amazon

    part_list = site_function(soup, part_name, site)

    return part_list


# functions for each site...
def paytmmall(soup, part_name, site):
    '''
        Function to scrape Part from paytmmall
        It returns a list of tuples in the order of title, price, link, img_link, websitename
        It takes Arguments BeautifulSoup object of paytmmall part search, part name
        '''

    items = soup.findAll("div", {"class": "_3WhJ"})
    part_list = []

    for i in items:
        try:

            title = i.a['title']
            price = "₹" + i.find("div", {"class": "_1kMS"}).span.text
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
        It returns a list of tuples in the order of title, price, link, img_link, websitename
        It takes Arguments BeautifulSoup object of flipkart part search, part name
        '''

    items = soup.findAll("div", {"class": "_1UoZlX"})
    part_list = []

    for i in items:
        try:

            title = i.find("div", {"class": "_3wU53n"}).text
            price = i.find("div", {"class": "_6BWGkk"}).find("div", {"class": "_1vC4OE _2rQ-NK"}).text
            link = "https://www.flipkart.com/" + i.a['href']
            img_link = "https://www.flipkart.com/" + i.find("div", {"class": "_1OCn9C"}).find("div", {'class': '_3BTv9X'}).img['src']
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
    #It returns a list of tuples in the order of title, price, link, img_link, websitename
    #It takes Arguments BeautifulSoup object of snapdeal part search, part name

    items = soup.findAll("div", {"class": "product-tuple-description"})
    part_list = []
    for i in items:
        try:
            title = i.find('p', {'class': 'product-title'}).text
            price = i.find('span', {'class': 'lfloat product-price'}).text
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
        It takes Arguments BeautifulSoup object of shopclues part search, part name
        '''

    items = soup.findAll("div", {"class": "column col3 search_blocks"})
    part_list = []

    for i in items:
        try:

            price = i.find("div", {"class": "ori_price"}).find("span", {"class": "p_price"}).text.replace('Rs.','₹')
            title = i.h2.text
            link = i.a['href']
            try:
                img_link = i.find('div', {'class': 'img_section'}).img['data-img']
            except:
                img_link = i.find('div', {'class': 'img_section'}).img['src']
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
        It returns a list of tuples in the order of title, price, link, img_link, websitename
        It takes Arguments BeautifulSoup object of croma part search, part name
        '''

    items = soup.findAll("div", {"class": "row"})
    part_list = []

    for i in items:
        try:

            title = i.find("div", {"class": "row", "style": " margin-right: 0;"}).find("a", {"class": "product__list--name"}).h3.text
            link = "https://www.croma.com" + i.find("div", {"class": "row", "style": " margin-right: 0;"}).a['href']
            price = i.find("div", {"class": "row", "style": " margin-right: 0;"}).find("div",{"class": "_priceRow"}).find("span", {"class": "pdpPrice"}).text
            img_link = i.find('div', {'class': 'col-md-2 col-xs-12 col-sm-3'}).picture.source['data-srcset']
            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, price, link,img_link, site))

        except:
            continue

    return part_list


def amazon(soup, part_name, site):
    '''
        Function to scrape Part from amazon
        It returns a list of tuples in the order of title, price, link, img_link, websitename
        It takes Arguments BeautifulSoup object of amazon.in part search, part name
        '''

    items = soup.findAll("div", {"class": "sg-col-inner"})
    part_list = []

    for i in items:
        try:

            title = i.find('a', {"class": "a-link-normal a-text-normal"}).find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
            price = "₹" + i.find("div", {"class": "a-row a-size-small"}).find('a', {'class': 'a-link-normal'}).find('span', {'class': 'a-size-base'}).text
            link = "https://amazon.in/"+i.find("div", {"class": "a-section a-spacing-none"}).find('a', {'class': 'a-link-normal'})['href'].strip()
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
