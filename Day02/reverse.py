# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:49:45 2019

@author: Lenovo
"""

def rev(string):
    length = len(string)
    for i in range(length-1,-1,-1):
        print(string[i],end='')
        
string = input("Enter any string>")
rev(string)



# Function to reverse a string
def reverse(input_string):
	# Reverse String
	return (input_string[::-1])

input_string = input("Enter a string >")
print (reverse (input_string))
