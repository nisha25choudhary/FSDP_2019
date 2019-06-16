# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:59:59 2019

@author: Lenovo
"""

def translet(string):
    vowel = 'aeiou '
    char1 =''
    for char in string:
        if char not in vowel:
            char1 = char1 +char+'o'+char
        else:
            char1 = char1+char
    print(char1)
    
translet('this is fun')



def translate(string):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    final_list = []

    for element in string:
        if element in consonants: 
            final_list.append(element+"o"+element)
        else:
            final_list.append(element)

    return "".join(final_list)

user_input = input("Enter string to Translate: ")

print (translate(user_input))


