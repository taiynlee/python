# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:06:10 2018

@author: Tommy_Lee
"""

import pandas as pd
#第一種以dic的鍵值為行標題，自動加入數值為列標題
df=pd.DataFrame({"林大明":[65,92,78,83,70],"陳聰明":[90,72,76,93,56],\
"黃美麗":[81,85,91,89,77],"熊小娟":[79,53,47,94,80]})
print(df)

#第二種自行定義行標題與列標題
datas=[[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
indexs=["林大明","陳聰明","黃美麗","熊小娟"]
columns=["國文","數學","英文","自然","社會"]
df=pd.DataFrame(datas,columns=columns, index=indexs)
print(df)
df.columns=["體育","數學","英文","自然","社會"]
df.index=["蔡英文","陳聰明","黃美麗","熊小娟"]
print(df)

print(df["體育"])
print(df[["體育","社會"]])
print(df[df.數學>80])
print(df.values)
print(df.values[0])
print(df.values[0][3])
"""
loc先列標籤再行標籤
"""
print(df.loc["蔡英文"]["數學"])
print(df.loc[("蔡英文","熊小娟"),:])
#iloc
print(df.iloc[1,:])
print(df.iloc[1,1])
print(df.iloc[1][1])
"""
改變值
"""
df.iloc[1][1]=73
print(df.iloc[1][1])

print(df.head(2))
print(df.tail(2))

"""
排序
True表示遞增排序 False表示遞減排序
"""
dfsort=df.sort_values(by="數學",ascending=True)
print(dfsort)

"""
刪除列 刪除欄 axis預設是0
"""
df1=df.drop("陳聰明")
print(df1)
df2=df.drop("數學",axis=1)
print(df2)
df3=df.drop(df.index[1:3])
print(df3)

"""
import data
read_csv
read_excel
read_sql (sqlite)
read_json
read_html (read_html會使用到html5lib conda install html5lib and import html5lib)
"""
tables=pd.read_html("http://www.stockq.org/market/commodity.php")
#print(tables)
table=tables[7]
table=table.drop(table.index[[0,1]])
table.columns=(["商品","買價","漲跌","比例","台北"])
table.index=range(len(table.index))
print(table)

"""
pandas繪圖 df.plot()
"""
datas=[[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
indexs=["林大明","陳聰明","黃美麗","熊小娟"]
columns=["國文","數學","英文","自然","社會"]
df=pd.DataFrame(datas,columns=columns, index=indexs)
df.plot()
