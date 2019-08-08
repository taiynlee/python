# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:49:18 2018

@author: Tommy_Lee
"""

x="abcdefg"
'''
判斷a是否在x中
'''
print("a" in x)
print("a" not in x)

'''
將x重複n次連接x本身
'''
print(x*3,3*x)

'''
取得索引值i的元素
取得索引值i到j，間隔k的序列
'''
print(x[3])
print(x[0:6:2])

print(len(x))
print(min(x))
print(max(x))
'''
取得x中第一次出現c的索引值
累計x中出現a的個數
'''
print(x.index("c"))
print(x.count("a"))