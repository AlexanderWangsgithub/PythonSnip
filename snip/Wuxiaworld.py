# parse wuxiaworld novel
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

# -*- coding: UTF-8 -*-

url = "http://www.wuxiaworld.com/desolate-era-index/"
response = requests.get(url).content


def getChapterUrlList(url):
    chapter_url_list = re.findall(r"http://www.wuxiaworld.com/desolate-era-index/de[a-zA-Z0-9-]*", str(response))
    # pprint(chapter_url_list)
    return chapter_url_list


def hprint(soupx):
    print(soupx.prettify())


chapter_url = "http://www.wuxiaworld.com/desolate-era-index/de-book-1-chapter-1"
chapter_response = requests.get(chapter_url).content
# chapter_content = re.findall(r"<hr/>.*<hr/>", str(chapter_response))
# pprint(chapter_content)
# use BeautifulSoup but not reg
soup = BeautifulSoup(chapter_response, "lxml")
all = soup.body.find_all("p")
# pprint(all)
for index in range(len(all)):
    if index in [0, 1,2]:
        continue
    p = all[index]
    if str.__contains__(str(), "Book") and p.span.strong != None:
        s1 = str.replace(str(p.span.strong), "<strong>", "")
        s2 = str.replace(s1, "</strong>", "")
        print(s2)
        continue
    if str.__contains__(str(p), "Chapter") and p.span.strong != None:
        s1 = str.replace(str(p.span.strong), "<strong>", "")
        s2 = str.replace(s1, "</strong>", "")
        print(s2)
        continue
    if str.__contains__(str(p), "class") and p.findAll("href") != None:
        break
    p1 = str.replace(str(p), "<p>", "")
    p2 = str.replace(p1, "</p>", "")
    if str.__contains__(p2, "<br/>"):
        str.__repr__(p2, "<br/>","")
    print(p2 + "\n")
