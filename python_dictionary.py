# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:35:46 2018

@author: Tommy_Lee
"""

tel={"justin":"0929837467","ivy":"0987276342"}
#取得key裏的value
print(tel["justin"])
print(tel.get("justin"))
#增加元素
tel["johny"]="00956234876"
print(tel)
#刪除元素
del tel["johny"]
print(tel)
print(list(tel.keys()))
print(tel.keys())
print(sorted(tel.keys()))
print("ivy" in tel)
print(len(tel))
print(tel.values())



