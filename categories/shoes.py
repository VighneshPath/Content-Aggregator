#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


part_sites={
    "+":[("libertyshoes","https://www.libertyshoesonline.com/liberty/st-search?q=shoes=item goes here"),
         ("buyhatke","https://compare.buyhatke.com/pricelist/big-fox-casual-shoes-price-in-india-hatke335504=item goes here")]
}


def scrape_site(site, part_name, soup):
    if(site == "libertyshoes"):
        site=libertyshoes
    elif(site == "buyhatke"):
        site=buyhatke
    part_list=site(soup, part_name)
    return part_list


def libertyshoes(soup, part_name):
    results=soup.findAll("div",{"class":"best-box"})
    part_list=[]
    for item in results:
        try:
            title=item.find("div",{"class":"info-box"}).a.h3.getText().strip()
            #print(title)
            price=item.find("div",{"class":"info-box"}).p.span.getText().strip()
            #print(price)
            link=item.find("div",{"class":"info-box"}).a['href'].strip()
            #print(link)
            #img_link=item.a.img['data-src'].strip()
           # print(img_link)
            for value in part_name:
                if(value not in title):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link))
        except:
            continue
    return part_list


def buyhatke(soup,part_name):
    results=soup.findAll("div",{"class":"results-product product"})
    for item in results:
        try:
            title=item.find("div",{"class":"padding-horizontal-1x"}).h3.getText().strip()
            #print(title)
            price=item.find("span",{"class":"product-price--value"}).b.getText().strip()
           # print("Rs."+price)
            link='https://compare.buyhatke.com/'+item.a['href'].strip()
            #print('https://compare.buyhatke.com'+link)
           # img_link=item.find("div",{"class":"product-img--wrap"}).img['data-original'].strip()
            #print(img)
            for value in part_name:
                if(value not in title):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link))
        except:
            continue            
    return part_list







