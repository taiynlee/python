# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:51:39 2018

@author: Tommy_Lee
"""

'''
集合元素不可以複製也沒有順序
集合是用來儲存沒有重複的元素

'''
s=set([1,2,3,4,5,6,7,7])
print(s)
#加一個元素
s.add("f")
print(s)

#移掉元素
s.remove("f")
print(s)

'''
且運算
或運算
對稱差運算
差運算
'''
s1={1,2,3,4}
print(s & s1)
print(s.intersection(s1))

print(s | s1)
print(s.union(s1))

print(s ^ s1)
print(s.symmetric_difference(s1))

print(s - s1)
print(s.difference(s1))

'''
判斷s是否為s1的真子集
判斷s是否為s1的子集
'''
print(s < s1)
print(s.issubset(s1))

print(s <= s1)

#s的烤貝
s2=s.copy()
print(s2)