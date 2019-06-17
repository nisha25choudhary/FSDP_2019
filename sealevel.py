# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:11:23 2019

@author: Lenovo
"""

 
import csv
year = []
inch = []
with open('sealevel.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
      #print(row)
      if row[0] == 'Year':
          continue
      else:
          
          year.append(int(row[0]))
          inch.append(float(row[1]))
#print(year)
#print(inch)

from matplotlib import pyplot as plt
#x label 
plt.xlabel("Years",fontsize = 15)
#y label
plt.ylabel("Inches",fontsize = 15)
plt.title("Survey sea level rise ")
plt.axis([1880,2015,0,10])
plt.plot(year,inch,label='sea level')
plt.legend()


plt.show()
