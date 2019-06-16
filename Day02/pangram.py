# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:05:47 2019

@author: Lenovo
"""

def pangram(string):
    list2 = []
    list1 = 'qwertyuioplkjhgfdsazxcvbnm'
    for i in string:
        if i not in list2:
            if i != ' ':
                list2.append(i)
            else:
                continue
        
    if len(list1) == len(list2):
        return " Pangram string"
    else:
        return " Not pangram string"

            
string = input("Enter any sentance which contain all alphabates>").lower()
print(pangram(string))

 



# To check if a string is pangram or not
input_string = input("Enter the string :")
count = 0
_list = []
_lower = input_string.lower()
for alpha in _lower:
    _list.append(alpha)

# remove duplicates
final_list = []    

for num in _list: 
 if num not in final_list: 
  final_list.append(num) 
    
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")
    
