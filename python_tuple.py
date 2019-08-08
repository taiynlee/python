# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:53:03 2018

@author: Tommy_Lee
"""

'''
也可以從字串來建立數組
'''
tp=tuple("abcdefg")
print(tp)
tp1=tuple([2*x for x in range(1,8)])
print(tp1)
'''
tuple相加
'''
tp2=tp+tp1
print(tp2)
print(type(tp2))