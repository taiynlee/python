# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:39:59 2018

@author: Tommy_Lee
"""

import re

"""
.  代表一個除了換列字元(\n)以外的所有字元
^  代表輸入列的開始
$  代表輸入列的結束
*  代表前一個項目可以出現0次或無限多次
+  代表前一個項目可以出現1次或無限多次
?  代表前一個項目可以出現0次或1次
[abc]  代表一個符合a或b或c的任何字元
[a-z]  代表一個符合a到z的任何字元
\  代表後面的字元以一般字元處理
{m}   代表前一個項目正好出現m次
{m.}  代表前一個項目最少出現m次，最多出現無限多次
{m,n}  代表前一個項目最少出現m次，最多出現n次
\d  一個數字字元，相當於[0123456789]或[0-9]
^  反運算，例如[^a-d]，代表除了abcd外的所有字元
\D  一個非數字的字元，相當於[^0-9]
\n  換行
\r  回到首字元
\t  tab定位字元
\s  空白字元，相當於[\r\t\n\f]
\S  非空白字元，相當於[^\r\t\n\f]
\w  一個數字 字母或底線字元，相當於[0-9a-zA-Z]
\W  一個非數字 字母或底線字元，相當於[^\w]，即[^0-9a-zA-Z]
=======================================================
整數  [0-9]+
小數  [0-9]+\.[0-9]+
英文字  [A-Za-z]+
變數名稱  [A-Za-z_][A-Za-z0-9_]*
EMAIL  [A-Za-z0-9_]+@[A-Za-z0-9\._]+
URL  http://[a-zA-Z0-9\./_]+
"""

m=re.match(r"[a-z]+","tem12po")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m=re.search(r"[a-z]+","tem12po")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

mlist=re.findall(r"[a-z]+","tem12po")
print(m)

