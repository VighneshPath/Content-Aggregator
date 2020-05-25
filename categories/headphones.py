from bs4 import BeautifulSoup
import requests

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

parts_sites ={"%20":[("www.flipkart.com" , "https://www.flipkart.com/search?q=item goes here")] , "+":[("www.snapdeal.com" , "https://www.snapdeal.com/search?keyword=item goes here"),("www.amazon.in", "https://www.amazon.in/s?k=item goes here")] , "-":[("www.headphonezone.in" , "https://www.headphonezone.in/collections/item goes here")]
}


'''elif(site == "www.ebay.com"):
    site_function = ebay'''


def scrape_site(site, part_name, soup):

    if(site == "www.amazon.in"):
        site_function = amazon
    elif(site == "www.flipkart.com"):
        site_function = flipkart
    elif(site == "www.snapdeal.com"):
        site_function = snapdeal

    part_list = site_function(soup, part_name, site)
    return part_list

# #HEADPHONEZONE

# url = "https://www.headphonezone.in/collections/bluetooth-wireless-earphones"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")

# def headphonezone(soup , part_name , site):
#     part_list = []
#     results = soup.find_all("div" , {"class":"product-wrap"})
#     for item in results:
#         try:
#             result = item.find("div" , {"class":"product-details"})

#             link = item.a["href"]

#             title = result.find("span" , {"class":"title"}).get_text().strip()

# 			price = result.find("span" , {"class":"money"}).get_text().strip().replace("Rs.","₹")

#             img = item.div.a["href"]

#             flag = 0

#             for word in part_name.split(" "):
#                 if(word not in title.lower().split()):
#                     flag = 1
#                     break
#             if(flag == 0):
#                     part_list.append((title,price,link,img,site))


#         except:
#             continue

#     return part_list



def amazon(soup , part_name , site):
    part_list = []
    results = soup.findAll("div", {"class": "a-section a-spacing-medium"})
    for result in results:
        try:
            title = result.find("span" , {"class":"a-size-medium a-color-base a-text-normal"}).get_text().strip()

            price = result.find("span", {"class": "a-offscreen"}).get_text().strip().replace("Rs.", "₹")

            link = "https://amazon.in" + \
                result.find("a", {"class": "a-link-normal a-text-normal"})['href'].strip()

            img = result.find("div", {"class": "a-section aok-relative s-image-fixed-height"}).img["src"]

            flag = 0
            for word in part_name.split(" "):

                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                    part_list.append((title,price,link,img,site))




        except:
            continue

    return part_list











# # FLIPKART

# url = "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=05654bd0-e28d-4421-a42f-328d90a25cd2&sort=popularity"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")
def flipkart(soup , part_name , site):
    part_list = []

    results = soup.find_all("div" , {"class":"_3liAhj"})

    for result in results:
        try:
            title = result.find("a" , {"class":"_2cLu-l"}).get_text().strip()

            price = result.find("div" , {"class":"_1vC4OE"}).get_text().strip().replace("Rs.","₹")

            link_ = result.find("a" , {"class":"Zhf2z-"})
            link = link_["href"]

            img_ = result.find("a" , {"class":"Zhf2z-"})
            img = img_["href"]

            link_ = result.find("a" , {"class":"_2cLu-l"})
            link = link_["href"]

            flag = 0

            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                    part_list.append((title,price,link,img,site))
        except:
            continue
    return part_list


# # SANPDEAL

# # url = "https://www.snapdeal.com/search?keyword=headphones&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"

# # html = requests.get(url)


# # soup = BeautifulSoup(html.text , "html.parser")
# def snapdeal(soup , part_name , site):

# 	results = soup.find_all("div" , {"class":"product-tuple-description"})

# 	for item in results:
# 		try:
# 			result = item.find("div" , {"class":"product-desc-rating"})

# 			title = result.a.p.get_text().strip()

# 			price = result.find("span" , {"class":"lfloat product-price"}).get_text().strip()

# 			img_ = item.find("img" , {"class":"product-image"})
# 			img = img_["src"]

# 			link = result.a["href"]

# 			flag = 0

# 			for word in part_name.split(" "):
# 				if(word not in title.lower().split()):
# 					flag = 1
# 					break
# 				if flag == 0:
# 					part_list.append((title,price,link.img,site))
# 		except:
# 			continue

# 	return part_list

# soup = BeautifulSoup(html.text , "html.parser")
def snapdeal(soup , part_name , site):
    part_list = []

    results = soup.find_all("div" , {"class":"product-tuple-description"})

    for item in results:
        try:
            result = item.find("div" , {"class":"product-desc-rating"})

            title = result.a.p.get_text().strip()

            price = result.find("span" , {"class":"lfloat product-price"}).get_text().strip().replace("Rs.","₹")

            img_ = item.find("img" , {"class":"product-image"})
            img = img_["src"]

            link = result.a["href"]

            flag = 0

            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                    part_list.append((title,price,link.img,site))
        except:
            continue

    return part_list



# # # EBAY

# # url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=headphones&_sacat=0"

# # html = requests.get(url)

# # soup = BeautifulSoup(html.text , "html.parser")

# def ebay(soup , part_name , site):

# 	results = soup.find_all("div" , {"class":"s-item__wrapper clearfix"})

# 	for result in results:
# 		try:
# 			title = result.find("h3" , {"class":"s-item__title"}).get_text().strip()

# 			price = result.find("div" , {"class":"s-item__detail s-item__detail--primary"}).span.get_text().strip()

# 			link = result.find("a" , {"class":"s-item__link"})["href"]

# 			flag = 0

# 			for word in part_name.split(" "):
# 				if(word not in title.lower().split()):
# 					flag = 1
# 					break
# 				if flag == 0:
# 					part_list.append((title,price,link))

# 		except:
# 			continue

# 	return part_list


