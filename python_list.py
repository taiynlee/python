# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:20:29 2018

@author: Tommy_Lee
"""
fruits=["orange","apple","pear","banana","kiwi","apple","banana"]
#計算元數出現的個數
print(fruits.count("apple"))
#回傳元素在list最小的索引值
print(fruits.index("banana"))
print(fruits.index("banana",4))
#倒轉順序
fruits.reverse()
print(fruits)
#把元素加到list最後
fruits.append("grape")
print(fruits)
#排序
fruits.sort()
print(fruits)
#list相加
fruits.extend(["berry","apple"])
print(fruits)
#將元素插入list索引值i的地方
fruits.insert(1,"berry")
print(fruits)
#移除list中第1個元素
fruits.remove("berry")
print(fruits)
'''
因為串列屬於堆疊，先進後出，所以pop會取出最後一個元素
'''
print(fruits.pop())
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
'''
佇列部份我們使用collections裏的deque
'''
from collections import deque
queue=deque(["阿呆","ERIC","JOHN","MICHAEL","小寶","小文"])
queue.append("TERRY")
queue.append("GRAHAM")
print(queue.popleft())
print(queue.popleft())
print(queue.pop())
print(queue)

