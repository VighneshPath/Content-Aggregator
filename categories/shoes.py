#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


parts_sites={
    "+":[("www.libertyshoesonline.com","https://www.libertyshoesonline.com/liberty/st-search?q=shoes=item goes here"),
         ("www.compare.buyhatke.com","https://compare.buyhatke.com/pricelist/big-fox-casual-shoes-price-in-india-hatke335504=item goes here"),
          ("www.fashos.com","https://www.fashos.com/catalogsearch/result/?q=penny+loafer+shoes=item goes here"),
          ("www.flipkart.com","https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off=item goes here")
         ]
}


def scrape_site(site, part_name, soup):
    if(site == "www.libertyshoesonline.com"):
        site_function=libertyshoes
    elif(site == "www.compare.buyhatke.com"):
        site_function=buyhatke
    elif(site=="www.fashos.com"):
        site_function=fashos
    elif(site=="www.flipkart.com"):
        site_function=flipkart
    part_list=site_function(soup, part_name,site)
    return part_list


def libertyshoes(soup, part_name,site):
    results=soup.findAll("div",{"class":"best-box"})
    part_list=[]
    for item in results:
        try:
            title=item.find("div",{"class":"info-box"}).a.h3.getText().strip()
            price=item.find("div",{"class":"info-box"}).p.span.getText().strip().replace("Rs.","₹")
            link=item.find("div",{"class":"info-box"}).a['href'].strip()
            img_link=item.a.img['data-src']
            flag=0
            for value in part_name.split(" "):
                if(value not in title.lower().split()):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link,img_link,site))
        except:
            continue
    return part_list


def buyhatke(soup,part_name,site):
    results=soup.findAll("div",{"class":"results-product product"})
    part_list=[]
    for item in results:
        try:
            title=item.find("div",{"class":"padding-horizontal-1x"}).h3.getText().strip()
            price="₹"+item.find("span",{"class":"product-price--value"}).b.getText().strip()
            link='https://compare.buyhatke.com/'+item.a['href'].strip()
            img_link=item.find("div",{"class":"product-img--wrap"}).img['data-original']
            flag=0
            for value in part_name.split(" "):
                if(value not in title.lower().split()):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link,img_link,site))
        except:
            continue            
    return part_list

def fashos(soup,part_name,site):
    results=soup.findAll("div",{"class":"product-item-info"})
    part_list=[]
    for item in results:
        try:
            title=item.find("div",{"class":"product details product-item-details"}).find("strong",{"class":"product name product-item-name"}).find("a",{"class":"product-item-link"}).getText().strip()
            price=item.find("span",{"class":"price-wrapper"}).find("span",{"class":"price"}).getText().strip().replace("Rs.","₹")
            link=item.a['href'].strip()
            img_link=item.a.img['src']
            flag=0
            for value in part_name.split(" "):
                if(value not in title.lower().split()):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link,img_link,site))
        except:
            continue
    return part_list

def flipkart(soup,part_name,site):
    results=soup.findAll("div",{"class":"IIdQZO _1SSAGr"})
    part_list=[]
    for item in results:
        try:
            title=item.find("div",{"class":"_2B_pmu"}).getText().strip()
            price=item.find("div",{"class":"_1uv9Cb"}).find("div",{"class":"_1vC4OE"}).getText().strip()
            link="https://www.flipkart.com/"+item.a['href'].strip()
            # img_link=item.find("div",{"class":"_3ZJShS _31bMyl"}).img['alt src'] 
            flag=0
            for value in part_name.split(" "):
                if(value not in title.lower().split()):
                    flag=1
                    break
            if(flag==0):
                part_list.append((title,price,link,site))
        except:
            continue  
    return part_list  

