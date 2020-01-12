import requests
from bs4 import BeautifulSoup
import re

def scrapByKeyword(keyword, url):
    webResource = requests.get(url+keyword)
    soup = BeautifulSoup(webResource.content,'html5lib')
    # print(soup.title)
    if isKeywordPresent(soup,keyword):
        return {url+keyword:filterByTag(soup,keyword)}
    else:
        return ""

def isKeywordPresent(soup,keyword):
    # print(keyword)
    # print(soup)
    res = soup.find_all(text=keyword) 
    # print(res)
    if keyword in res:
        return True
    else:
        return False

def filterByTag(soup,keyword):
    res = soup.find_all('p')
    resultset = []
    # print(res)
    for x in res:
        # print(x)
        # print(x)
        # print(str(x).find(keyword))
        if keyword in str(x):
            # print('found: ')
            resultset.append(str(x))
            # return str(x)
    return resultset

def readConf(fileName):
    separator = "="
    keys={}

    with open(fileName) as f:
        for line in f:
            if separator in line:
                name,value = line.split(separator,1)
                keys[name.strip()] = value.strip()

    # print(keys)
    return keys                    

def scrapResults():
    urls = readConf("conf")
    keywords = readConf("keywords")
    for url in urls:
        # print(url)
        for kw in keywords:
            print(scrapByKeyword(keyword = keywords[kw],url = urls[url]))

# readConf()
scrapResults()