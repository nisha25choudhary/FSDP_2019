# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:53:56 2019

@author: Lenovo
"""

from PIL import Image, ImageDraw, ImageFont
   
image = Image.open('Screenshot (5).png')# create Image object with the input image
  
draw = ImageDraw.Draw(image)# the image object as background
font = ImageFont.truetype('arial.ttf', size=20)
 
#company name  
(x, y) = (48, 190)
message = ' Company Name: '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)  

(x, y) = (220, 190)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)
#image.save(str(company)+'.png')

font = ImageFont.truetype('arial.ttf', size=15)
# Random  ID NO
import random

(x, y) = (60, 220)
message = ' ID No.  : '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)  

# adding an unique id number. You can manually take it from user by input function
(x, y) = (180, 220)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
draw.text((x, y), message, fill=color, font=font)

#student name  
(x, y) = (60, 250)
message = ' Your Name: '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font) 

(x, y) = (180, 250)
message = input('Enter Your Full Name: ')
name=message
color = 'rgb(0, 0, 0)' # black color
draw.text((x, y), message, fill=color, font=font)

#date of brith
(x, y) = (60, 280)
message = ' DOB : '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font) 


(x, y) = (180, 280)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)

#E-mail ID
(x, y) = (60, 310)
message = ' E-mail ID : '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font) 


(x, y) = (180, 310)
message = input('Enter Your E-mail ID : ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)

#Mobile NO
(x, y) = (60, 340)
message = ' Mobile No.  : '
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font) 


(x, y) = (180, 340)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


image.save(str(company)+'.png')
