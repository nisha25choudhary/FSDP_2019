# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:26:17 2019

@author: Lenovo
"""

student_list = []

while True:
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)
