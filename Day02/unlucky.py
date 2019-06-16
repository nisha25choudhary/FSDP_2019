# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:14:08 2019

@author: Lenovo
"""

list1 = input("Enter any no>").split(",")

co = 0
for num in range(len(list1)):
     if list1[num] == 13 and list1[num] != 13:
         var = True
         
     else:
         co = co + list1[num]
         
print(co)

 


user_input = input("Enter comma seperated nos >").split(",")

previous_number_is_13 = False
total = 0

for number in user_input:
    if int(number) == 13:
        previous_number_is_13 = True
    
    elif not previous_number_is_13:
        total += int(number)
    
    elif previous_number_is_13 and int(number) != 13:
        previous_number_is_13 = False

print (total)


 