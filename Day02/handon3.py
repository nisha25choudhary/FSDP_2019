# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:38:51 2019

@author: Lenovo
"""

def days_in_month(m):
    if m=='Jan' or m=='March' or m=='May' or m=='July' or m=='Aug' or m=='Oct' or m=='Dec' :
        return 31
    elif m=='Fed':
        return 28
    
    elif m=='Apr' or m=='June' or m=='Sep' or m=='Nov'  :
        return 30
     
    
month = input("Enter Month name'Jan,Feb,March,Apr,May,June,July,Aug,Sep,Oct,Nov,Dec'>")
print("Days in month:",days_in_month(month))
    
    
    
    
    
    
    
    
    