# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:50:48 2018

@author: Tommy_Lee
"""
"""
os提供建立目錄 刪除目錄 刪除檔案 執行作業系統命令等方法
"""
import os
file="file.txt"
if os.path.exists(file):
    #os.remove(file)
    pass
else:
    print(file+"已建立")
print(os.path)

dir="doc"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("已經存在")

if os.path.exists(dir):
    os.rmdir(dir)
"""
執行作業系統命令system()
"""
os.system("mkdir doc")
os.system("rmdir doc")
"""
path裏的方法
"""
fulname=os.path.abspath(file)
print(os.path.abspath(file))
print(os.path.isabs(file))
print(os.path.isfile(file))
print(os.path.split(fulname))
print(os.path.splitdrive(fulname))
