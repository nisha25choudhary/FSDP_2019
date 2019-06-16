# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:27:53 2019

@author: Lenovo
"""
   
            
list1 = ['Alabama','California','Oklahoma','Florida']
            
vowel = 'aeiouAEIOU'
main_list = []
#length = len(list1)
for i in list1:
    list2 = []
    for each_char in i:
        if each_char not in vowel:
            list2.append(each_char) 
    main_list.append("".join(list2))
print (main_list)




state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiou')

final_list = []

for state in state_name:
    state_elements = list(state.lower())
    
    for element in vowels:
        while element in state_elements:
            state_elements.remove(element)
    final_list.append("".join(state_elements))

print (final_list)





#version 02
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiouAIEOU')

final_list = []

for name in state_name:
    temp_list = []
    for char in name:
        if char not in vowels:
            temp_list.append(char)
    final_list.append("".join(temp_list))

print (final_list)            


