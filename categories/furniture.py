#import requests
#from bs4 import BeautifulSoup


parts_sites = {
    "+": [("www.amazon.in", "https://www.amazon.in/s?k=item goes here"), ("www.pepperfry.com", "https://www.pepperfry.com/site_product/search?q=item goes here")]
}


def scrape_site(site, part_name, soup):
    if(site == "www.amazon.in"):
        site_function = amazon
    elif(site == "www.pepperfry.com"):
        # print("PPF")
        site_function = pepperfry
    part_list = site_function(soup, part_name, site)
    return part_list


def amazon(soup, part_name, site):
    results = soup.findAll("div", {"class": "a-section a-spacing-medium"})
    part_list = []
    for item in results:
        try:
            title = item.find("span", {
                              "class": "a-size-base-plus a-color-base a-text-normal"}).get_text().strip()
            price = "₹" + item.find(
                "span", {"class": "a-price-whole"}).get_text().strip()
            link = "https://amazon.in" + \
                item.find(
                    "a", {"class": "a-link-normal a-text-normal"})['href'].strip()
            img_link = item.find("img", {"class": "s-image"})['src']
            # print(title, price, link, img_link)
            f = 0
            #print(title, part_name)
            for product in part_name.split(" "):
                if(product not in title.lower().split()):
                    f = 1
                    break
            if(f == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list


def pepperfry(soup, part_name, site):
    results = soup.findAll(
        "div", {"class": "clip-crd-10x11 pf-white srch-rslt-bxwrpr"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "div", {"class": "pf-col xs-12"}).h2.a.text.strip(" ")
            link = item.find(
                "div", {"class": "pf-col xs-12"}).h2.a["href"]

            price = item.find(
                "span", {"class": "clip-offr-price"}).text.strip().replace("Rs.", "₹")

            img_link = item.find(
                "div", {"class": "card-img-wrp center-xs card-srch-img-wrp"}).a.img["data-src"]
            f = 0
            for product in part_name.split(" "):
                if(product not in title.lower().split()):
                    f = 1
                    break
            if(f == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return(part_list)
