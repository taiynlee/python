# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:57:51 2018

@author: Tommy_Lee
"""

import requests
from bs4 import BeautifulSoup
"""
sp=BeautifulSoup(原始碼,"html.parser")
"""

url="http://www.taiwanlottery.com.tw/"
html=requests.get(url)
html.encoding="UTF-8"
sp=BeautifulSoup(html.text,"html.parser")

"""
title  傳回網頁標題，如sp.title
text  傳回去除所有html標籤後的網頁文字內容
find()  傳回第一個符合條件的tag
find_all()  傳回所有符合條件的tag
select()  傳回指定的css如id或class的內容 id前面要加# class前面要加.
"""
#讀取title
datal=sp.select("title")
print(datal)
#讀取class
datal=sp.select(".title")
print(datal)
#讀取id
datal=sp.select("#rightdown")
print(datal)
#讀取tag
datal=sp.select("html head title")
print(datal)

print(sp.find("a"))
print(sp.find_all("a"))
links=sp.find_all(["a","img"])
for link in links:
    href=link.get("href")
    if href != None and href.startswith("http://"):
        print(href)
        
print(sp.find_all("a",{"id":"link1"}))