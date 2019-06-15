# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:22:45 2019

@author: Lenovo
"""

from PIL import Image, ImageDraw, ImageFont


image_obj = Image.open("png//sign.jpeg").convert('L')
cropped_image = image_obj.crop((710,80,1010, 190))
cropped_image.save('logo.jpg')
cropped_image.show()


image_obj = Image.open("png//sign.jpeg").convert('L')
cropped_image = image_obj.crop((130,980,390, 1200))
cropped_image.save('sign.jpg')
cropped_image.show()



image_obj = Image.open("png//sign.jpeg").convert('L')
cropped_image = image_obj.crop((770,985,940,1125))
cropped_image.save('seal.jpg')
cropped_image.show()

img = Image.open("png//camp.jpg")
img2 = Image.open('seal.jpg')
w,h = img2.size
#print(w,h)
img2 = img2.resize((w-50,h-50))
w1,h1 = img2.size
#print(w1,h1)'''
img2.save('re.jpg')

img.paste(img2,(20,330))
img.save("paste.jpg")
img.show()



img = Image.open("paste.jpg")
img2 = Image.open('sign.jpg')
w,h = img2.size
#print(w,h)
img2 = img2.resize((w-90,h-100))
#w1,h1 = img2.size
img2.save('re.jpg')
#img2.show()
img.paste(img2,(290,310))
img.save("sign.png")
img.show()



'''
img = Image.open("sign.png")
img2 = Image.open('logo.jpg')
w,h = img2.size
print(w,h)
img2 = img2.resize((w-130,h-5))
#w1,h1 = img2.size
img2.save('re.jpg')
#img2.show()
img.paste(img2,(125,320))
img.save("logo.png")
img.show()
'''

   
image = Image.open('sign.png')# create Image object with the input image
  
draw = ImageDraw.Draw(image)# the image object as background
font = ImageFont.truetype('arial.ttf', size=20)

(x, y) = (100, 122)
message = input('\nEnter Your Name: ')
name=message
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

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
