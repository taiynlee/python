# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:51:32 2018

@author: Tommy_Lee
"""

x=123
print(x)
type(x)
y=123.32
type(y)
9//3.3
9%3
name="sa due"
A=70.126
B=60.8
score=A+B
print("%s score =%10.2f and %.2f all=%d" % (name,A,B,score))

print("{} all the scrore{}".format(name,score))
letters="abcdefghijklmnopqrstuvwxyz"
len(letters)
letters[:-1:2]
todos="geta,getb,getc,getd"
todos.split(",")
todos_01=('yeti','bigfoot','loch ness monster')
todos01_str=','.join(todos_01)
print(todos01_str)
empty_list=[]
print(empty_list)

import matplotlib.pyplot as plt

listx=[1,5,7,9,13,16]
listy=[15,50,80,40,70,50]
plt.plot(listx,listy)
plt.show()
listx1=[2,6,8,11,14,16]
listy1=[10,40,30,50,80,60]
plt.plot(listx1,listy1,color="blue", linewidth="5", linestyle="-", label="Female")
plt.legend(loc="upper left")
plt.xlim(0,20)
plt.ylim(0,100)
plt.title("Pocket Money")
plt.xlebel("Age")
plt.yLebel("Money")
plt.show()
#plt.show()

labels=["東","南","北","中"]
sizes=[5,10,20,15]
colors=["red","green","blue","yellow"]
explode=(0,0,0.05,0)
plt.pie(sizes,explode=explode,labels=labels,\
        colors=colors,labeldistance=1.1,\
        autopct="%2.1f%%",shadow=True,\
        startangle=90,pctdistance=0.6)
plt.axis("equal")
plt.legend()
plt.show()

from bokeh.plotting import figure, show

p = figure(width=800, height=400)
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
p.line(listx, listy)
show(p)

import numpy as np
x=np.linspace(0,10,100)
#fig=plt.figure()
plt.plot(np.sin(x),"-")
plt.plot(np.cos(x),"--")
np.sin(x)

rng=np.random.RandomState(0)
for marker in['o','.',',','x','+','v','^','v','<','>','s','d']:
    plt.plot(rng.rand(5), rng.rand(5),marker,label='marker={}'.format(marker))
plt.legend(shadow=True)
plt.xlim(0,1.8)

from sklearn import datasets
import matplotlib.pyplot as plt
digits=datasets.load_digits()
fig=plt.figure(figsize=(4,5))
fig.subplots_adjust(left=0,right=1,bottom=0, top=1,hspace=0.05, wspace=0.05)
for i in range(20):
    ax=fig.add_subplot(5,4,i+1, xticks=[],yticks=[])
    ax.imshow(digits.images[i],cmap=plt.cm.binary)
    ax.text(0,7,str(digits.target[i]))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
rng=np.random.RandomState(42)
x=10*rng.rand(50)
x
y=2*x-1+rng.randn(50)
plt.scatter(x,y)

from sklearn.linear_model import LinearRegression
X=x[:,np.newaxis]
X.shape
X
y
model=LinearRegression(fit_intercept=True)
model.fit(X,y)
model.coef_
model.intercept_
xfit=np.linspace(-1,11)
xfit

x1=10*rng.rand(5)
y1=2*x1-1+rng.randn(5)
x1
y1
xfit=np.linspace(-1,11)
xfit
Xfit=xfit[:,np.newaxis]
yfit=model.predict(Xfit)
plt.scatter(x,y)
plt.plot(xfit,yfit)
x.shape
x
X
len(xfit)
y.shape

from sklearn.datasets import load_iris
iris_dataset=load_iris()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=1)
iris_dataset['data']
iris_dataset['target']

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,y_train)
y_model=model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_model)

import seaborn as sna
iris=sna.load_dataset("iris")
iris.head()

X_iris=iris.drop("species",axis=1)
from sklearn.decomposition import PCA
model=PCA(n_components=2)
model.fit(X_iris)
X_2D=model.transform(X_iris)
import seaborn as sns
iris
X_2D
iris['PCA1']=X_2D[:,0]
iris['PCA2']=X_2D[:,1]
iris
sns.lmplot('PCA1','PCA2',hue='species',data=iris,fit_reg=False);

from sklearn.datasets import load_digits
digits=load_digits()
digits.images.shape
type(digits)
digits.keys()

import pandas as pd
data=pd.DataFrame(digits["data"])
data

import matplotlib.pyplot as plt
fig, axes=plt.subplots(10,10,figsize=(8,8),subplot_kw={'xticks':[],'yticks':[]})
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i],cmap='binary',interpolation='nearest')
    ax.text(0,0.05,str(digits.target[i]),transform=ax.transAxes, color='green')

x=digits.data
y=digits.target
x.shape
y.shape
from sklearn.manifold import Isomap
iso=Isomap(n_components=2)
iso.fit(digits.data)
data_projected=iso.transform(digits.data)
data_projected.shape

import matplotlib.pyplot as plt
plt.scatter(data_projected[:,0],data_projected[:,1],c=digits.target
        ,edgecolors='none',alpha=0.5,cmap=plt.cm.get_cmap('nipy_spectral',10));    
plt.colorbar(label='digit label',ticks=range(10))
plt.clim(-0.5,9.5)

pdrain=pd.read_csv("rain.csv")
pdrain
pdrain.keys()
type(pdrain)
pdprcp=pdrain["PRCP"]
listrain=list()
for a in pdprcp:
    if a ==0:
        listrain.append(0)
    else:
        listrain.append(1)

listrain


listrain.count(0)/len(listrain)
listrain.count(1)/len(listrain)

No_Rain=listrain.count(0)
Rain=listrain.count(1)
objects=["Rain","NO_Rain"]
number=np.arange(len(objects))
number
No_Rain
Rain
listnumber=(Rain,No_Rain)

plt.bar(number, listnumber, align='center', alpha=0.5)
plt.xticks(number, objects)
plt.ylabel('day_count')
plt.title('Rainy day of a year')
#plt.legend(loc='upper left')
width = 0.75 # the width of the bars 
ind = np.arange(listrain.count(0))  # the x locations for the groups
ax.set_yticks(ind+width/2)
plt.show()

1+1
