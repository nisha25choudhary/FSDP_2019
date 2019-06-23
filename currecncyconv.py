# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:09:34 2019

@author: Lenovo
"""

'https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=c959833b4e78e0ad4606'





import requests

url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=c959833b4e78e0ad4606"
response = requests.get(url)
jsondata = response.json()
doller = int(input("Enter doller currency:>"))
print("Currency in rupees:",round(doller*jsondata["USD_INR"],2))
#print (jsondata["USD_INR"])





import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR"
url3 = "&compact=y"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content


print (response.text)
print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))

for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


# Content in binary form
print (type(response.content))

print ("Content or Response Body : " + str(response.content))


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
# response has the original JSON String
# jsondata has the convert string in the python data type dictionary

print (str(type(jsondata)))

print (jsondata)

print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
conversion_price = jsondata["USD_INR"]["val"]

# take USD value from user as input
user_input_in_USD = int(input("Enter the USD value :"))

# convert USD to INR
USD_to_INR = user_input_in_USD * conversion_price

print ("{0} USD in INR is {1} RS".format(user_input_in_USD, round(USD_to_INR,2)))
