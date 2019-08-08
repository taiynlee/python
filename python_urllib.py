# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:54:38 2018

@author: Tommy_Lee
"""

from urllib.parse import urlparse

url="http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1"
o=urlparse(url)
print(o)
"""
ParseResult(scheme='http', netloc='taqm.epa.gov.tw:80', path='/pm25/tw/PM25A.aspx', params='', query='area=1', fragment='')
"""
print("scheme={}".format(o.scheme))
print("netloc={}".format(o.netloc))
print("port={}".format(o.port))
print("path={}".format(o.path))
print("query={}".format(o.query))
