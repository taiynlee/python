# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:05:02 2018

@author: Tommy_Lee
"""

import sqlite3

conn=sqlite3.connect("test.sqlite")
sqlstr="insert into test (id,name) values('5','76')"
conn.execute(sqlstr)
conn.commit()
conn.close()

conn=sqlite3.connect("test.sqlite")
sqlstr="select * from test"
cursor=conn.execute(sqlstr)
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()

conn=sqlite3.connect("test.sqlite")
sqlstr="select * from test"
cursor=conn.execute(sqlstr)
row=cursor.fetchone()
print(row)
conn.close()