# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:50:14 2019

@author: Lenovo
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
#print (url)


response = requests.get(url)
#print (type(response.content))
#print ("Status code: " + str(response.status_code))
#print ("Headers : " + str(response.headers))
#print ("Data : " + response.text)

jsondata = response.json()

print("Latitude :",jsondata["coord"]["lat"]) 
print("Longitude :",jsondata["coord"]["lon"]) 
print("Weather Condition :",jsondata["weather"]) 
print("Wind speed :",jsondata["wind"]["speed"]) 
print("Sunset Rise  :",jsondata["sys"]["sunrise"]) 
print("Set timing :",jsondata["sys"]["sunset"]) 

#print (jsondata)

 