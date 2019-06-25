# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:22:08 2019

@author: Lenovo
"""
"""people = [{'name': 'Mary', 'height': 160},
         {'name': 'Isla', 'height': 80},
         {'name': 'Sam'}]
height_total = 0
height_count = 0
for person in people:
     if 'height' in person:
         height_total += person['height']
         height_count += 1

     if height_count > 0:
         average_height = height_total / height_count
print (average_height)"""

from functools import reduce
 
people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},{'name': 'Sam'}]

l = list(filter(lambda x: 'height' in x,people))
x = reduce(lambda a,b:a+b ,map(lambda x:x['height'],l))
res = x / len(l)
print(res)




people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)




from functools import reduce 

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = list( map(lambda x: x['height'],filter(lambda x: 'height' in x, people)))

if len(heights) > 0:
    average_height = reduce(lambda x,y : x+y, heights) / len(heights)
    
print(average_height)    
    

