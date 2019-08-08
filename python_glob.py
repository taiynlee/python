# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:09:17 2018

@author: Tommy_Lee
"""

"""
glob套件可以取得指定條件的檔案串列
"""

import glob
files=glob.glob("file.txt")+glob.glob("python*.py")+glob.glob("*.txt")
for file in files:
    print(file)