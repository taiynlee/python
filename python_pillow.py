# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:08:06 2018

@author: Tommy_Lee
"""

from PIL import Image,ImageColor
"""
(255,255,255)RGB, (255,255,255,255)第四個代表透明度
紅色(255,0,0)
綠色(0,128,0)
藍色(0,0,255)
白色(255,255,255)
"""
myim=Image.new("RGBA",(100,100))
myim.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myim.putpixel((i,j),ImageColor.getcolor("red","RGBA"))

print("1")
print(myim.getpixel((0,0)))
print("2")
print(myim.getpixel((0,50)))
myim.save("Pixel_1.png")

myim=Image.new("RGBA",(100,100))
myim.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myim.putpixel((i,j),(255,255,255))
        
for i in range(100):
    for j in range(50,100):
        myim.putpixel((i,j),ImageColor.getcolor("blue","RGBA"))
print("1")
print(myim.getpixel((0,0)))
print("2")
print(myim.getpixel((0,50)))
myim.save("Pixel_2.png")

logo="python-02.png"
logoim=Image.open(logo)
width,heigh=logoim.size
print(width,heigh)
print(logoim.filename)
print(logoim.format)
print(logoim.format_description)
logoim.save("python-02.jpg")

"""
切割圖片
"""
logo="python-02.png"
logoim=Image.open(logo)
width,heigh=logoim.size
print(width,heigh)
"""
(5500,2000)到(6500,3000)的座標
"""
logoim=logoim.crop((5500,2000,6500,3000))
logoim.save("mycrop.png")
width,heigh=logoim.size
print(width,heigh)

"""
拷貝圖片
"""
logo="python-02.png"
logoim=Image.open(logo)
mycopy=logoim.copy()
width,heigh=logoim.size
print(width,heigh)
logoim=logoim.crop((6000,2000,7000,3000))
mycopy.paste(logoim,(100,100))
mycopy.paste(logoim,(2000,2000))
mycopy.save("new_fixed.png")

"""
調整圖片大小
"""
logo="python-02.png"
logoim=Image.open(logo)
width,heigh=logoim.size
print(width,heigh)
logoim1=logoim.resize((int(width/4),int(heigh/4)))
print(logoim1.size)
logoim1.save("half_fixed.png")

"""
翻轉圖片
"""
logoim.rotate(180).save("rotate_180.png")
"""
圖片水平左右翻轉
"""
logoim.transpose(Image.FLIP_TOP_BOTTOM).save("hori_flip.png")

"""
在目錄裏的圖片都加浮水印
"""
import os
picture=Image.open("PNG.png")
picture.resize((300,300))
for filename in os.listdir("."):
    if not (filename.endswith(".png") or filename.endswith(".jpg")):
        continue
    im=Image.open(filename)
    im.paste(picture,(500,500))
    im.save(os.path.join("image",filename))
    