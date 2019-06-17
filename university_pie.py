# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:59:54 2019

@author: Lenovo
"""

import csv
data = {}
with open('University_data.csv','rt') as uni:
    reader = csv.reader(uni,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in data:
            data[i[0]] += int(i[1])
        else:
            data[i[0]] = int(i[1])
#print(zoo_data) #show total requirement of water 
name = list(map(lambda x: x ,data.keys()))
#print(name)  #show all keys
score = list(map(lambda x: x ,data.values()))
#print(score) #show all values

from matplotlib import pyplot as plt

 
plt.xlabel("University names",fontsize = 15)
#y label
plt.ylabel("Scores",fontsize = 15)
explode = (0, 0, 0, 0,0.2)  # explode 1st slice to 10% of the radius

plt.title("Survey university score ")
plt.pie(score,labels = name,wedgeprops={'edgecolor':'black'},autopct='%.0f%%',explode = explode)

plt.axis('equal')  
plt.show()
 
 