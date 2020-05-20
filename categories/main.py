import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
}


@dataclass
class Part():
    '''
    Class to Represent a Part from a given website
    '''
    title: str
    price: str
    link: str
    img_link: str
    site: str

    def get_price(self):
        try:
            return float(''.join(self.price[1:].split(",")))
        except:
            return 0

    def __str__(self):
        return(f"Part name: {self.title}\nPrice: {self.price}\nWebsite: {self.link}\nImage Link: {self.img_link}")


def get_search_url(part_name, site, space_separator):
    search_url = site.replace(
        "item goes here", space_separator.join(part_name.split()))
    return search_url


def get_soup(url):
    response = requests.get(url, headers=headers)
    if(response.status_code == requests.codes.ok):
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    else:
        return


def part_list_threading(site, part_name, space_separator, sites_part_list, file):
    search_url = get_search_url(part_name, site[1], space_separator)
    site_soup = get_soup(search_url)
    if(site_soup != None):
        temp_part_list = file.scrape_site(site[0], part_name, site_soup)
        part_list = []
        for part in temp_part_list:
            part_list.append(Part(part[0], part[1], part[2], part[3], part[4]))
    else:
        part_list = []
    sites_part_list.extend(part_list)
    return


def sort_according_to_price(part_list):
    '''
    Function to sort The part list according to Price
    It returns a list of Part Objects sorted ascendingly accordingly to their price
    It takes one argument of Unsorted list of Part Objects
    '''
    price_sort = []
    for item in part_list:
        price_sort.append((item.get_price()))
    price_sort.sort()
    new_part_list = []
    for price in price_sort:
        for item in part_list:
            if(item.get_price() == price):
                new_part_list.append(part_list.pop(part_list.index(item)))
    return new_part_list


def get_part_list(part_name, part_cat):
    if(part_cat == "Computer Parts"):
        import categories.computer_parts
        file = categories.computer_parts
    elif(part_cat == "Mobiles"):
        import categories.mobile
        file = categories.mobile
    elif(part_cat == "Headphones"):
        import categories.headphones
        file = categories.headphones
    elif(part_cat == "Furniture"):
        import categories.furniture
        file = categories.furniture
    elif(part_cat == "Shoes"):
        import categories.shoes
        file = categories.shoes
    # A list to store All the list of Part Objects
    sites_part_list = []
    # Creating List for Storing Threads for each site
    threads = []
    for space_separator, url in file.parts_sites.items():
        for a_site in url:
            thread_obj = threading.Thread(target=part_list_threading, args=[
                                          a_site, part_name, space_separator, sites_part_list, file])
            threads.append(thread_obj)
            thread_obj.start()
    for thread in threads:
        # Waiting for all the threads to complete
        thread.join()
    sites_part_list = sort_according_to_price(sites_part_list)
    return sites_part_list
