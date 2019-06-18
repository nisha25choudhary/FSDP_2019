# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:58:49 2019

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (len(incomes))
 
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
 

#plt.hist(incomes,bins=50) 
plt.hist(incomes,bins=list(range(10,500,10))) 
plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.show()



incomes = np.append(incomes, [-1000000])
print("Median value is: ", np.median(incomes))
print("Mean value is: ", np.mean(incomes))
plt.hist(incomes,bins=50) 
plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.show()
