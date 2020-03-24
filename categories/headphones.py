'''
1. Sennheiser
2. Headhonezone
3. Bajjao
'''


from bs4 import BeautifulSoup
import requests

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

headers = headers


#BAJAAO

# url = "https://www.bajaao.com/pages/findify-search-results?q=headphones"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")

# results = soup.find_all("div" , {"class":"findify-components-common--grid_column"})
# print(results)




# #HEADPHONEZONE

# url = "https://www.headphonezone.in/collections/bluetooth-wireless-earphones"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")

# results = soup.find_all("div" , {"class":"product-wrap"})
# print(results)

# for item in results:
# 	try:
# 		result = item.find("div" , {"class":"product-details"})

# 		title = result.find("span" , {"class":"title"})
# 		print(title.text)

# 		price = result.find("span" , {"class":"money"})
# 		print(price.text)

# 		link = item.a["href"]
# 		print(link)

# 		img = item.div.a["href"]
# 		print(img)
# 	except:
# 		continue


# # FLIPKART

# url = "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_10_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=05654bd0-e28d-4421-a42f-328d90a25cd2&sort=popularity"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")

# results = soup.find_all("div" , {"class":"_3liAhj"})
# # print(results)

# for result in results:
# 	try:
# 		title = result.find("a" , {"class":"_2cLu-l"}).get_text().strip()
# 		print(title)

# 		price = result.find("div" , {"class":"_1vC4OE"}).get_text().strip()
# 		print(price)

# 		link_ = result.find("a" , {"class":"Zhf2z-"})
# 		link = link_["href"]
# 		print(link)

# 		img = result.find()
# 	except:
# 		continue

# # SANPDEAL

# url = "https://www.snapdeal.com/search?keyword=headphones&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"

# html = requests.get(url)

# soup = BeautifulSoup(html.text , "html.parser")

# results = soup.find_all("div" , {"class":"product-tuple-description"})

# for item in results:
# 	try:
# 		result = item.find("div" , {"class":"product-desc-rating"})

# 		title = result.a.p.get_text().strip()
# 		print(title)

# 		price = result.find("span" , {"class":"lfloat product-price"}).get_text().strip()
# 		print(price)

# 	# 	img_ = item.find("img" , {"class":"product-image"})
# 	# 	img = img_["src"]
# 	# 	print(img)

# 		link = result.a["href"]
# 		print(link)
# 	except:
# 		continue

# # EBAY

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=headphones&_sacat=0"

html = requests.get(url)

soup = BeautifulSoup(html.text , "html.parser")

results = soup.find_all("div" , {"class":"s-item__wrapper clearfix"})

for result in results:
	try:
		title = result.find("h3" , {"class":"s-item__title"}).get_text().strip()
		print(title)

		price = result.find("div" , {"class":"s-item__detail s-item__detail--primary"}).span.get_text().strip()
		print(price)

		link = result.find("a" , {"class":"s-item__link"})["href"]
		print(link)
		
	except:
		continue




