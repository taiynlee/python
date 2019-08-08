# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:00:16 2018

@author: Tommy_Lee
"""

import sqlite3,ast,requests
from bs4 import BeautifulSoup

conn=sqlite3.connect("DataBasePM25.sqlite")
sqlstr="""
create table if not exists TablePM25 ("no" integer primary key autoincrement 
not null unique , "SiteName" text not null, "PM25" integer)
"""
cursor=conn.execute(sqlstr)
print("建立成功")

url="http://opendata.epa.gov.tw/ws/Data/ATM00625/?$select=Site,PM25&$skip=0&$top=1000&format=json"
html=requests.get(url).text.encode("utf-8-sig")
print(html)

sp=BeautifulSoup(html,"html.parser")
jsondata=ast.literal_eval(sp.text)
print(jsondata)
print(type(html))

conn.execute("delete from TablePM25")
conn.commit()

n=1
for site in jsondata:
    SiteName=site["Site"]
    PM25=0 if site["PM25"]=="" else int(site["PM25"])
    sqlstr="insert into TablePM25 values({},'{}',{})".format(n,SiteName,PM25)
    cursor.execute(sqlstr)
    n+=1
    conn.commit()
conn.close()