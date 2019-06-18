# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:11:42 2019

@author: Lenovo
"""

import numpy as np 
import collections

#import random 

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        #res.append(random.randint(start, end)) 
        #res.append(np.random.uniform(start,end))
        res.append(np.random.randint(start,end)) #with np generate 40 random no
        collection = collections.Counter(res) #without np calculate frequency
        arr = np.array(np.unique(res, return_counts=True)).T #with np calculate frequency
    print("Random Array of 40 integer:  ")
    print(len(res))
    print(res)
    print("Frequency of numbers without np:   ")
    print(collection)
    print("Frequency of numbers with np    ")
    print(arr)
    #return res,collection,arr
  
# Driver Code 
num = 40
start = 5
end = 15
#print(Rand(start, end, num)) 
Rand(start, end, num)
