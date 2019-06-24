# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:15:35 2019

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
    else:
         result.append(False)
#print(result)
print(any(result))


numbers  = input("Enter space seprated Numbers>").split(" ")

print(any([num == num[::-1] for num in numbers]))



# give list of inputs from user
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
