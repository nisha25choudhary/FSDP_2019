# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:16:58 2019

@author: Lenovo
"""
import collections

import csv
leng = []
reader = csv.DictReader(open("bardata.csv"))
for raw in reader:
    #print(raw)
    #print(raw['LanguagesWorkedWith'].split(';'))
     
    for item in raw['LanguagesWorkedWith'].split(';'):
        #print([item])
        leng.append(item)
#print(leng)
collection = collections.Counter(leng)
#print(c1)
collection = dict(collection) # store decresing order of dict data
value_list = list(collection.values())
key_list = list(collection.keys())

value = sorted(value_list)[-10:] #store top 10 values

new_list = list(zip(value_list,key_list))
new_list = sorted(new_list)[-10:]   
key = []
for val in new_list:
    #print(val)
    a,b = val
    #print(b)
    key.append(b) #store top 10 values of keys
    

import matplotlib.pyplot as plt
 
plt.xlabel('Uses')

plt.ylabel('Language')

plt.title('See top 10 more useful language')
#plt.yticks(fontsize=10)
 
plt.barh(key, value, align='center', alpha=1.0)


plt.show()

   