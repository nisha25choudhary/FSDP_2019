# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:58:39 2019

@author: Lenovo
"""

 
import csv
dict1 ={}
with open("population.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    p1 = 0
    for row in csv_reader:            
            if row['State or union territory'] not in dict1:
                dict1[row['State or union territory']] = float(row['Population'].replace(',',''))
            else:
                dict1[row['State or union territory']] += float(row['Population'].replace(',',''))
                 
for k,v in dict1.items():
    print("{Key:"+"India,"+k+" value: ",v,'}')
        
 

import csv
with open('population.csv') as pop:
    r = csv.reader(pop, delimiter=',')
    next(r)
    dict1 = {}
    for record in r:
        if dict1.get(record[3]):
            value = record[2].replace(',','')
            dict1["India,"+record[3]] += int(value)
        else:
            value = record[2].replace(',','')
         
print(dict1) 