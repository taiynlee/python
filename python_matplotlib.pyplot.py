# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:54:45 2018

@author: Tommy_Lee
"""

import matplotlib.pyplot as mpt

month1=[1,2,3,4,5,8,10,12]
month2=[1,3,4,5,6,7,11,12]
sales1=[20000,40000,60000,80000,100000,120000,140000,160000]
sales2=[10000,20000,30000,150000,120000,80000,60000,210000]

mpt.plot(month1,sales1,lw=2,label="ivy lin")
mpt.plot(month2,sales2,lw=2,label="johny wu")
mpt.xlabel("month")
mpt.ylabel("dollars(million)")
mpt.legend()
mpt.title("matplotlib_example")
mpt.show()

import matplotlib.pyplot as plt
# bo 紅色圓點 r--紅色虛線 bs藍色矩形 g^綠色三角形
plt.plot([1,2,3,4],[1,4,9,16],"ro")
plt.ylabel("some numbers")
plt.show()

import matplotlib.pyplot as plot
import numpy as np
t=np.arange(0.,5.,0.2)
plot.plot(t,t,"r--",t,t**2,"bs",t,t**3,"g^")
plot.show()

mpt.bar(month1,sales1,lw=2,label="ivy lin")
mpt.bar(month2,sales2,lw=2,label="johny wu")
mpt.xlabel("month")
mpt.ylabel("dollars(million)")
mpt.legend()
mpt.title("matplotlib_example")
mpt.show()

labels=["East","South","Notth","Center"]
sizes=[5,10,20,15]
colors=["red","green","blue","yellow"]
explode=(0,0,0.05,0)#突出
"""
autopct  項目百分比格式 語法為%格式%% 如2.1表示整數2位 小數1位
pctdistance  百分比文字與圓心的距離是半徑的多少倍
"""
plt.pie(sizes,explode=explode,labels=labels,colors=colors,labeldistance=1.1,autopct="%3.1f%%",shadow=True,startangle=90,pctdistance=0.6)
plt.axis("equal")#正圓形
plt.legend()
plt.show()

"""
BOKEN套件的特色是圖表以網頁呈現
"""

from bokeh.plotting import figure,show,output_file

output_file("bokehlineout.html")
p=figure(width=800, height=400,title="statistics")
#===============
p.title.text_color="green"
p.title.text_font_size="18pt"
p.xaxis.axis_label="month"
p.xaxis.axis_label_text_color="violet"
p.yaxis.axis_label="sales"
p.yaxis.axis_label_text_color="violet"
dashs=[12,4]#虛線
#===============
p.line(month1,sales1,line_width=4,line_color="red",line_alpha=0.3,line_dash=dashs,legend="figure")
show(p)


"""
散點圖
"""
output_file("bokehcircleout.html")
p=figure(width=800, height=400,title="statistics")
#===============
p.title.text_color="green"
p.title.text_font_size="18pt"
p.xaxis.axis_label="month"
p.xaxis.axis_label_text_color="violet"
p.yaxis.axis_label="sales"
p.yaxis.axis_label_text_color="violet"
sizes=[10,20,30,40,30,20,40,10]
colors=["red","blue","green","pink","violet","gray","black","brown"]
#===============
p.circle(month1,sales1,size=sizes,color=colors,alpha=0.5)
#p.square(month1,sales1,size=sizes,color=colors,alpha=0.5)
#p.cross(month1,sales1,size=sizes,color=colors,alpha=0.5)
#p.triangle(month1,sales1,size=sizes,color=colors,alpha=0.5)
#p.square_cross(month1,sales1,size=sizes,color=colors,alpha=0.5)
show(p)