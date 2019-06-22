# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:33:55 2019

@author: Lenovo
"""
from PIL import Image
from io import BytesIO
import requests

 

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)

img=Image.open(BytesIO(response.content))
img.save("forsk-tech.png")




from PIL import Image
import requests
from io import BytesIO

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("forsk-logo.png")


# Alternate Solution
"""
import requests

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
with open("forsk-logo.png","wb") as f:
    f.write(response.content)
"""