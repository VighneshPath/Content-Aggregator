#import requests
#from bs4 import BeautifulSoup


parts_sites = {
     "+":[("www.amazon.in","https://www.amazon.in/s?k=item goes here")],
     "%20":[("www.flipkart.com","https://www.flipkart.com/search?q=item goes here")],
     "+":[("www.pepperfry.com","https://www.pepperfry.com/search?q=item goes here")]
}

def scrape_site(site, part_name, soup):
    if(site == "www.amazon.in"):
        site_function = amazon
    elif(site == "www.flipkart.com"):
        site_function = flipkart
    elif(site == "www.pepperfry.com"):
        site_function = pepperfry
    part_list = site_function(soup,part_name,site)
    return part_list

def amazon(soup,part_name,site):
    results = soup.findAll("div",{"class":"a-section a-spacing-medium"})
    part_list=[]
    for item in results:
        try:
            title = item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).get_text().strip()
            price = item.find("span", {"class": "a-price-whole"}).get_text().strip()
            link = "https://amazon.in" + item.find("a", {"class": "a-link-normal a-text-normal"})['href'].strip()
            img_link = item.find("img",{"class":"s-image"})
            f=0
            for product in part_name:
                if(product not in title):
                    f=1
                    break
            if(f==0):
                part_list.append((title,price,link,img_link))   
        except:
            continue
    return  part_list               

def flipkart(soup,part_name,site):
    results = soup.findAll("div",{"class":"bhgxx2 col-12-12"})
    part_list=[]
    for item in results:
        try:
            title=item.find("a",{"class":"_2cLu-l"}).get_text().strip()
            price=item.find("div",{"class":"_1vC4OE"}).get_text().strip()
            link = "https://flipkart.com"+ item.find("a",{"class":"_2cLu-l"})['href'].strip()
            img_link = item.find("img",{"class":"_1Nyybr  _30XEf0"})['src']
            f=0
            for product in part_name:
                if(product not in title):
                    f=1
                    break
            if(f==0):
              part_list.append((title,price,link,img_link))   
        except:
            continue
    return part_list

def pepperfry(soup,part_name,site):
    results = soup.findAll("div",{"class":"pf-col srchrslt-crd-10x11 srch-rslt-cards pf-margin-bottom20 clipprods"})
    part_list=[]
    for item in results:
        try:
            title=(item.find("a",{"class":"clip-prd-dtl"}).text)
            link="https://www.pepperfry.com/"+(item.find("a",{"class":"clip-prd-dtl"})['href'])
            price = (item.find("div",{"class":"clip-price-blocks row"}).find("span",{"class":"clip-offr-price"}).text.strip())
            img_link = item.find("div",{"class":"card-img-wrp center-xs card-srch-img-wrp"}).img['src']
            f=0
            for product in part_name:
                if(product not in title):
                    f=1
                    break
            if(f==0):
                part_list.append((title,price,link,img_link))
        except:
            continue
    return(part_list) 






