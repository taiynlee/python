# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:59:36 2018

@author: Tommy_Lee
"""
"""
mode的第一個字代表操作r w a
第二個字代表檔案的類型b代表binary，t代表文字
with open("file.txt","r",encoding="UTF-8") as f:
with open("file.txt","r",encoding="cp950") as f:
"""

fp=open("file.txt","w")
if fp!=None:
    print("檔案開啟成功")
    fp.write("test")
else:
    print("找不到檔案")
fp.close()

fp0=open("file.txt","at")
if fp0!=None:
    print("檔案開啟成功")
    fp0.write("test")
else:
    print("找不到檔案")
fp0.close()

fp1=open("file.txt","r")
if fp1!=None:
    str=fp1.read()
    print(str)
fp1.close()

fp2=open("file.txt","r")
if fp2!=None:
    #讀到list中
    str=fp2.readlines()
    print(str)
fp2.close()

binaryData=bytes(range(0,128))
print(len(binaryData))
fout=open("BinaryFile","wb")
fout.write(binaryData)
fout.close()

filein=open("BinaryFile","rb")
bdata=filein.read()
print(len(bdata))
for i in bdata:
    print(bdata[i])
filein.close()

"""
with運算式as變數
"""
with open("Binaryfile","rb") as filein:
    bdata=filein.read()
    print(len(bdata))
    for i in bdata:
        print(bdata[i])
