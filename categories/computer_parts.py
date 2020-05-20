parts_sites = {
    "%20": [("www.vedantcomputers.com", "https://www.vedantcomputers.com/index.php?route=product/search&search=item goes here&description=true")],
    "+": [("www.amazon.in", "https://www.amazon.in/s?k=item goes here"), ("www.mdcomputers.in", "https://mdcomputers.in/index.php?category_id=0&search=item goes here&submit_search=&route=product%2Fsearch"), ("www.primeabgb.com", "https://www.primeabgb.com/?post_type=product&taxonomy=product_cat&s=item goes here"), ("www.theitdepot.com", "https://www.theitdepot.com/search.html?keywords=item goes here")]
}


def scrape_site(site, part_name, soup):
    '''
    Function to call Parts Scraper for respective Site
    It returns list of Part objects corresponding to the given part name in a respective site
    It takes arguments site name, part name, BeautifulSoup object of site
    '''
    if(site == "www.mdcomputers.in"):
        site_function = mdcomp
    elif(site == "www.amazon.in"):
        site_function = amazon
    elif(site == "www.vedantcomputers.com"):
        site_function = vedcomp
    elif(site == "www.primeabgb.com"):
        site_function = primeabgb
    elif(site == "www.theitdepot.com"):
        site_function = theitdepot
    part_list = site_function(soup, part_name, site)
    return part_list


def theitdepot(soup, part_name, site):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of tuples in the order of title, price, link, img_link, websitename
    It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
    '''
    results = soup.findAll("div", {"class": "card card-white border-0 p-0"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "div", {"class": "card-text px-2 py-1 font-size85 product_title"}).a.text.strip()
            price = "₹" + item.find("div",
                                    {"class": "card-text px-2 py-1"}).strong.text.strip()
            link = "https://www.theitdepot.com/" + item.find("div",
                                                             {"class": "card-text px-2 py-1 font-size85 product_title"}).a["href"]
            img_link = item.find(
                "div", {"class": "product-image position-relative"}).a.img["src"]
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list


def mdcomp(soup, part_name, site):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of tuples in the order of title, price, link, img_link, websitename
    It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
    '''
    results = soup.findAll("div", {"class": "product-item-container"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "div", {"class": "right-block right-b"}).h4.a.get_text().strip()
            price = item.find(
                "span", {"class": "price-new"}).get_text().strip()
            link = item.find(
                "div", {"class": "right-block right-b"}).h4.a['href'].strip()
            img_link = item.find(
                "div", {"class": "product-image-container"}).a.img["data-src"]
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list


def amazon(soup, part_name, site):
    '''
    Function to scrape Part from amazon.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of amazon.in part search, part name
    '''
    results = soup.findAll("div", {"class": "a-section a-spacing-medium"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "span", {"class": "a-size-medium a-color-base a-text-normal"}).get_text().strip()
            price = item.find(
                "span", {"class": "a-offscreen"}).get_text().strip()
            link = "https://amazon.in" + \
                item.find(
                    "a", {"class": "a-link-normal a-text-normal"})['href'].strip()
            img_link = item.find(
                "div", {"class": "a-section aok-relative s-image-fixed-height"}).img["src"]
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list


def vedcomp(soup, part_name, site):
    '''
    Function to scrape Part from vedantcomputers.com
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of vedantcomputers.com part search, part name
    '''
    results = soup.findAll("div", {"class": "product-thumb product-wrapper"})
    part_list = []
    for item in results:
        try:
            title = item.find("h4", {"class": "name"}).get_text().strip()
            if(item.find("span", {"class": "price-new"}) == None):
                price = item.find("p", {"class": "price"}
                                  ).get_text().strip().strip()
            else:
                price = item.find(
                    "span", {"class": "price-new"}).get_text().strip()
            link = item.find("h4", {"class": "name"}).a['href']
            try:
                img_link = item.find(
                    "img", {"class": "lazy first-image"})["data"].replace(" ", "%20")
            except:
                img_link = item.find(
                    "img", {"class": "lazy first-image"})["data-src"].replace(" ", "%20")

            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list


def primeabgb(soup, part_name, site):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of primeabgb.com part search, part name
    '''
    results = soup.findAll("div", {"class": "product-inner equal-elem"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "div", {"class": "product-innfo"}).h3.a.get_text().strip()
            try:
                try:
                    price = item.findAll(
                        "span", {"class": "woocommerce-Price-amount amount"})[1].get_text().strip()
                except:
                    price = item.find(
                        "span", {"class": "woocommerce-Price-amount amount"}).get_text().strip()
            except:
                continue
            link = item.find(
                "div", {"class": "product-innfo"}).h3.a['href'].strip()
            img_link = item.find(
                "img", {"class": "attachment-post-thumbnail wp-post-image"})["src"]
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list
