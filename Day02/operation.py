# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:09:38 2019

@author: Lenovo
"""

def add(list1):
    total = 0
    for num in list1:
        total = total + int(num)
    return total
        
def multi(list1):
    total = 1
    for num in list1:
        total = total * int(num)
    return total
    
def largest(list1):
    num = list1[0]
    for i in list1:
        if num < i:
            num = i
    return num

def smallest(list1):
    num = list1[0]
    for i in list1:
        if num > i:
            num = i
    return num
            
def remove(list1):
    dup = []
    for num in list1:
        if num not in dup:
            dup.append(num)
    return dup
list1 = input("enter number>").split()
print('Sum = ',add(list1), '\nMultiply = ',multi(list1),'\nLargest = ',largest(list1),'\nSmallest = ',smallest(list1),'\nSorted = ',sorted(list1),'\nWithout Duplicate = ',remove(list1))
largest(list1)
smallest(list1)






def Add(lst):
    total = 0
    for i in lst:
        total += i
    return total

def Multiply(lst):
    product = 1
    for i in lst:
        product *= i
    return product

def Largest(lst):
    init = lst[0]
    for i in lst:
        if init < i:
            init = i
    return init

def Smallest(lst):
    init = lst[0]
    for i in lst:
        if init > i:
            init = i
    return init

def Sorting(lst):
    s = len(lst)
    us = True
    while us:
        us = False
        i = 0
        while i<s-1:
            if lst[i] > lst[i+1]:
                t = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = t
                us = True
            i += 1
    return lst

def Remove_Duplicates(lst):
    n_lst = []
    for i in lst:
        if i not in n_lst:
            n_lst.append(i)
    return n_lst

def Print(lst):
    lst = list(lst)
    print (Add(lst))
    print (Multiply(lst))
    print (Largest(lst))
    print (Smallest(lst))
    print (Sorting(lst))
    print (Remove_Duplicates(lst))

my_list = input("Enter list: ").split(",")

final_list = []

for i in my_list:
    final_list.append(int(i))
    
Print (final_list)

