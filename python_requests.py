# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:12:17 2018

@author: Tommy_Lee
"""

import requests

url="http://www.e-happy.com.tw"
html=requests.get(url)
html.encoding="UTF-8"
#print(html.text)
htmllist=html.text.splitlines()
for row in htmllist:
    print(row)
print(htmllist)

n=0
for row in htmllist:
    if "出版社書號" in row:
        n=n+1
print("找到共{}行".format(n))

