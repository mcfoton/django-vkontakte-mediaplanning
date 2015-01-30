# -*- coding: utf-8 -*-

import time

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
"""
browser = webdriver.Chrome()

browser.get("http://allsocial.ru/communities/?community=-1:-1")
time.sleep(1)

body = browser.find_element_by_tag_name("body")

html_source = browser.page_source


content = open('content.html', 'wb')
html_source.encode('utf-8')
content.write(html_source)
content.close()

browser.quit() 

'''
no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("post-item-title")

for post in post_elems:
    print post.text
'''
"""

#getting data from file
html_doc = open('content_test.html', 'r')
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

listoflists = []

#parsing the data
itemlist = soup.find_all("li", {"dr-communities-item": "", "ng-repeat": "item in list.communities"})

for item in itemlist:
    title = item.contents[0].find_all("a", {"bo-href": "item.href"})[0].text
    link = item.contents[0].find_all("a", {"bo-href": "item.href"})[0].get("href")
    
    tags = []
    taglist = item.contents[0].find_all("ul", {"class": "ui-cc-list"})[0]
    for tag in taglist.find_all("a"):
        tag.encode('utf-8')
        tags.append(tag.text)
    tags = u','.join(tags)

    members_count = item.contents[0].find_all("div", {"class": "quantity"})[0].text
    
    _reach_wrapper = item.contents[0].find_all("div", {"class": "reach-wrapper"})[0]
    reach = _reach_wrapper.find_all("a")[0].text
    
    _visitors_wrapper = item.contents[0].find_all("div", {"class": "visitors-wrapper"})[0]
    visitors = _visitors_wrapper.find_all("a")[0].text
    
    _delta = item.contents[0].find_all("div", {"class": "diff-wrapper"})[0]
    deltaabs = _delta.find_all("span", {"bo-text": "item.diff_abs | digitNumber"})[0].text
    deltaamp = _delta.find_all("span", {"bo-text": "(item.diff_rel | toFixedNumber | digitNumber) + '%'"})[0].text
    price =  item.contents[0].find_all("span", {"class": "cpp ng-binding"})[0].text

    listoflists.append([title, link, tags, members_count, reach, visitors, deltaabs, deltaamp, price])


#saving to csv
import unicodecsv as csv

with open("allsocial.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(listoflists)