# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:52:57 2019

@author: Lenovo
"""

import numpy as np

input_data = input("Enter 9 space seperated data:>") .split() #take input with space
#print(input_data)
input_data = [int(i) for i in input_data] #convert string to integer
nd_arr = np.array( input_data) #convert list into ndarray
#print (nd_arr)
#print (nd_arr.ndim)
 
nd_arr = nd_arr.reshape(3,3) #change dimension of ndarray
print (nd_arr)
