# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:03:22 2018

@author: Tommy_Lee
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

url="http://www.yahoo.com.tw"

html=requests.get(url)
html.encoding="UTF-8"

sp=BeautifulSoup(html.text,"html.parser")

images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

#all_links=sp.find(["a","img"])
all_links=sp.find_all(["a","img"])
print(all_links)

for link in all_links:
    src=link.get("src")
    print(src)
    href=link.get("href")
    print(href)
    attrs=[src,href]
    print(attrs)
    print("=============")
    for attr in attrs:
        if attr!=None and (".jpg" in attr or ".png" in attr):
            print("^^^^^")
            full_path=attr
            filename=full_path.split("/")[-1]
            print(full_path)
            print(filename)
            try:
                image=urlopen(full_path)
                f=open(os.path.join(images_dir,filename),"web")
                f.write(image.read())
                f.close()
            except:
                print("無法讀取")
                
    
