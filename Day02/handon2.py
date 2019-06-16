# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:35:05 2019

@author: Lenovo"""

def leap_year(year):
    if year%4==0 and year%400:
        return True
    else:
        return False
    
year = int(input("Enter any year>"))
print(leap_year(year))



def leapyr(n):
    if n % 4 == 0 and n % 100 != 0:
        if n % 400 == 0:
            print(n, " is a leap year.")
        else:
            pass
    elif n % 4 != 0:
        print(n, " is not a leap year.")
    else:
        pass
     
print(leapyr(2020))