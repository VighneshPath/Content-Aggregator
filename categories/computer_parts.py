parts_sites = {
    "%20":[("vedantcomputers","https://www.vedantcomputers.com/index.php?route=product/search&search=item goes here")],
    "+":[("amazon","https://www.amazon.in/s?k=item goes here"),("mdcomputers","https://mdcomputers.in/index.php?category_id=0&search=item goes here&submit_search=&route=product%2Fsearch"),("primeabgb","https://www.primeabgb.com/?post_type=product&taxonomy=product_cat&s=item goes here")]
}

def scrape_site(site, part_name, soup):
    '''
    Function to call Parts Scraper for respective Site
    It returns list of Part objects corresponding to the given part name in a respective site
    It takes arguments site name, part name, BeautifulSoup object of site
    '''
    if(site == "mdcomputers"):
        site = mdcomp
    elif(site == "amazon"):
        site = amazon
    elif(site == "vedantcomputers"):
        site = vedcomp
    elif(site == "primeabgb"):
        site = primeabgb
    part_list = site(soup, part_name)
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
            title = item.h4.a.get_text().strip()
            price = item.find("span",{"class":"price-new"}).get_text().strip()
            link = item.h4.a['href'].strip()
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title,price,link))
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
            title = item.find("span",{"class":"a-size-medium a-color-base a-text-normal"}).get_text().strip()
            price = item.find("span",{"class":"a-offscreen"}).get_text().strip()
            link ="https://amazon.in"+item.find("a",{"class":"a-link-normal a-text-normal"})['href'].strip()
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title,price,link))
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
            title = item.find("h4",{"class":"name"}).get_text().strip()
            if(item.find("span",{"class":"price-new"}) == None):
                price = item.find("p",{"class":"price"}).get_text().strip().strip()
            else:
                price = item.find("span",{"class":"price-new"}).get_text().strip()
            link = item.find("h4",{"class":"name"}).a['href']
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title,price,link))
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
            title = item.h3.a.get_text().strip()
            try:
                try:
                    price = item.findAll("span",{"class":"woocommerce-Price-amount amount"})[1].get_text().strip()
                except:
                    price = item.find("span",{"class":"woocommerce-Price-amount amount"}).get_text().strip()
            except:
                continue
            link = item.h3.a['href'].strip()
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title,price,link))
        except:
            continue
    return part_list
