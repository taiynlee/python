# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:44:06 2018

@author: Tommy_Lee
"""

"""
python提供hashlib套件可以判別文件是否更新過
"""
import hashlib
import requests
import os

md5=hashlib.md5(b"Test String!").hexdigest()
print(md5)

url="http://www.yahoo.com.tw"
html=requests.get(url).text.encode("utf-8-sig")
print(html)

md5=hashlib.md5(html).hexdigest()
old_md5=""
if os.path.exists("old_md5.txt"):
    with open("old_md5.txt","r") as f:
        old_md5=f.read()
    with open("old_md5.txt","w") as f:
        f.write(md5)
else:
    with open("old_md5.txt","w") as f:
        f.write(md5)
        old_md5=md5
        
if md5!=old_md5:
    print("已更新")
else:
    print("未更新或新寫入")
    