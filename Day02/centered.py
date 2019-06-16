# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:59:15 2019

@author: Lenovo
"""

list1 =  input("Enter any number>").split()
list1.pop()
list1.pop(0)

total = 0
for num in list1:
    total = total + int(num)
    avg = total // len(list1)
print(avg)



user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = []

for i in user_input:
    user_list.append(int(i))

# Sorting the list of integers
user_list.sort()

# leaving out 1 smallest and 1 largest value
final_list = user_list[1:-1]

# Calculating average
average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))


 