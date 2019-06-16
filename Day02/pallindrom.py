# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:21:40 2019

@author: Lenovo
"""
result = []
numbers  = input("Enter space seprated Numbers>").split(" ")
#print(first_list.reverse())
for num in numbers:
    num1 = num[::-1]
    #print(num1)
    if num == num1:
        result.append(True)
if len(result)>=1:
    print(True)
else:
    print(False)



numbers  = input("Enter space seprated Numbers>").split(" ")
if all([int(i)>0 for i in numbers]) and any([i==i[::-1] for i in numbers]):
    print ("True")
else:
    print ("False")





user_input = input("Enter space seperated values :").split()

input_length  = len(user_input)
count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True

print(pallindromic_integer)
