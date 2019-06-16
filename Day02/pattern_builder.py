# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:50:03 2019

@author: Lenovo
"""
 

num = int(input("Enter any integer no>"))
 
for i in range(0,num):
    print('*'*i)
for i in range(num,0,-1):
    print('*'*i)


# Enter Number to print pattern
num = int(input("Enter Number to print Pattern: "))

# Prints the upper half of the pattern
for i in range(1,num+1):
    print("*" * i)

# Prints the lower half of the pattern
for i in range(num-1,0,-1):
    print("*" * i)
    