# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:05:19 2019

@author: Lenovo
"""

def brick(list1):
    small_b = int(list1[0])
    large_b = int(list1[1])
    target = int(list1[2])
    
    small_b_inch = 1*small_b
    large_b_inch = 5*large_b
    total = small_b_inch + large_b_inch
    if target % 5 >  small_b:
        print("False")
    elif total > target:
        print("True")
        
list1 = input("enter 3 nunber in form 'small bricks,large bricks,target'>").split(" ")
 
brick(list1)



def make_bricks(small, big, goal):
    if goal % 5 > small:
        print (False) 
    else:    
        c = big*5 + small
        if c >= goal:
            print (True)
        else:
            print (False)

lst = input("Enter Numbers: ").split(",")

my_list=[]

for i in lst:
    my_list.append(int(i))
    
make_bricks(my_list[0], my_list[1], my_list[2])
