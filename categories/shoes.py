#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests              
from bs4 import BeautifulSoup as bs
res=requests.get("https://www.libertyshoesonline.com/")


soup=bs(res.text,"html.parser")
result=soup.findAll("div",{"class":"info-box"})
for i in result:
    try:
        title=i.a.h3.getText()
        print(title)
        price=i.p.span.getText()
        print(price)
    except:
        continue
         
         
         
         
         
         
         
         
         
         
         
         
         


# In[39]:


import requests
from bs4 import BeautifulSoup as bs
res=requests.get("https://www.flipkart.com/")
soup=bs(res.text,"html.parser")
result=soup.findAll("div",{"class":"_2kSfQ4"})
for i in result:
    try:
        title=i.a.getText()
        print(title)
        #price=i.find("div",{"class":"BXlZdc"})
        #print(price)
    except:
        continue


# In[48]:


import requests
from bs4 import BeautifulSoup as bs
res=requests.get("https://compare.buyhatke.com/pricelist/big-fox-casual-shoes-price-in-india-hatke335504")
soup=bs(res.text,"html.parser")
result=soup.findAll("div",{"class":"padding-horizontal-1x"})
for i in result:
    try:
        title=i.h3.getText()
        print(title)
         #price=i.find("div",{"class":"product-price u-textLeft padding-horizontal-1x"}).span.b.getText()
         #print(price)
    except:
        continue


# In[6]:


import requests
from bs4 import BeautifulSoup as bs
res=requests.get("https://www.amazon.in/s?k=shoes&ref=nb_sb_noss_2") 
soup=bs(res.text,"html.parser")
result=soup.findAll("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
for i in result:
    try:
        title=i.a.getText()
        print(title)
    except:
        continue


# In[ ]:




