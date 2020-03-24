import requests
from bs4 import BeautifulSoup


parts_sites = {
     "+":[("amazon","https://www.amazon.in/s?k=item goes here")],
     "%20":[("flipkart","https://www.flipkart.com/search?q=item goes here")]
}

def scrape_site(part_name,soup,site):
    if(site == "amazon"):
        site = amazon
    elif(site == "flipkart"):
        site = flipkart
    part_list = site(soup,part_name)
    return part_list

def amazon(soup,part_name):
    results = soup.findAll("div",{"class":"a-section a-spacing-medium"})
    for item in results:
        try:
            title = item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).get_text().strip()
            price = item.find("span", {"class": "a-price-whole"}).get_text().strip()
            link = "https://amazon.in" + item.find("a", {"class": "a-link-normal a-text-normal"})['href'].strip()
            f=0
            for product in part_name:
                if(product not in title):
                    f=0
                    break
            if(f==0):
                part_list.append((title,price,link))   
        except:
            continue
    return  part_list               

def flipkart(soup,part_name):
    results = soup.findAll("div",{"class":"bhgxx2 col-12-12"})
    for item in results:
        try:
            title=item.find("a",{"class":"_2cLu-l"}).get_text().strip()
            price=item.find("div",{"class":"_1vC4OE"}).get_text().strip()
            link = "https://flipkart.com"+ item.find("a",{"class":"_2cLu-l"})['href'].strip()
            f=0
            for product in part_name:
                if(product not in title):
                    f=0
                    break
            if(f==0):
              part_list.append((title,price,link))   
        except:
            continue
    return part_list






