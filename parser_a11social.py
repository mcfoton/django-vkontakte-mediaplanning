# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
listoflists = []

#working around pagination

url = 'http://allsocial.ru/communities/?community=-1:-1&order=quantity'
browser.get(url)
time.sleep(1)
html_source = browser.page_source

#trying the pagination to work
# browser.find_element_by_xpath("//table[last()]//td[last()]/a").click()
# browser.find_elements_by_xpath('//div[@class="paginator"]/div/div/ul/li/div')[1].click()


for page in range(1, 4):
    offset = (page-1)*25
    url = 'http://allsocial.ru/communities/?community=-1:-1&offset=' + str(offset) +  "&order=quantity"
    browser.get(url)
    time.sleep(1)
    html_source = browser.page_source
    print "Page %s loaded, " % page,

    #getting data from file
    # html_source = open('content_test.html', 'r')

    soup = BeautifulSoup(html_source)
    
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

        members_count = item.contents[0].find_all("div", {"class": "quantity"})[0].text.replace(" ", "")
        
        _reach_wrapper = item.contents[0].find_all("div", {"class": "reach-wrapper"})[0]
        reach = _reach_wrapper.find_all("a")[0].text.replace(" ", "")
        
        _visitors_wrapper = item.contents[0].find_all("div", {"class": "visitors-wrapper"})[0]
        visitors = _visitors_wrapper.find_all("a")[0].text.replace(" ", "")
        
        _delta = item.contents[0].find_all("div", {"class": "diff-wrapper"})[0]
        deltaabs = _delta.find_all("span", {"bo-text": "item.diff_abs | digitNumber"})[0].text.replace(" ", "")
        try:
            deltaamp = _delta.find_all("span", {"bo-text": "(item.diff_rel | toFixedNumber | digitNumber) + '%'"})[0].text
        except:
            deltaamp = _delta.find_all("span", {"bo-switch-default": ""})[0].text
           
        price =  item.contents[0].find_all("span", {"class": "cpp ng-binding"})[0].text

        listoflists.append([title, link, tags, members_count, reach, visitors, deltaabs, deltaamp, price])
    print "%s items in the list" % len(listoflists)

browser.quit()

#saving to csv
import unicodecsv as csv

with open("allsocial.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(listoflists)