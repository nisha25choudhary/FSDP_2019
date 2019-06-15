# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:25:09 2019

@author: Lenovo
"""


from PIL import Image, ImageDraw, ImageFont
  
image = Image.open('sign.png')# create Image object with the input image
  
draw = ImageDraw.Draw(image)# the image object as background
font = ImageFont.truetype('arial.ttf', size=20)

#Add your Name
(x, y) = (100, 122)
message = input('\nEnter Your Name: ')
name=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

#Add Program name
(x, y) = (150, 180)
message = input('\nEnter Program Name: ')
n=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

(x, y) = (200, 226)
message = input('\nEnter Company Name Which conduct This Program: ')
n=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

(x, y) = (170, 270)
message = input('\nEnter Month: ')
n=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)


(x, y) = (280, 270)
message = input('\nEnter Day: ')
n=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)


(x, y) = (410, 270)
message = input('\nEnter Year: ')
n=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

image.save(str(name)+'.png')
