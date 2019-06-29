# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:46:22 2019

@author: Lenovo
"""


import re
    
str_n = input("Enter card no>").split(",")



for var in str_n:
    res = re.match(r"^[4-6](\d{15}|\d{3}\-(\d{4}\-){2}\d{4})$", var)
    res1 = re.search(r"(\d)\1{3,}", var.replace("-",""))
    if res and not res1:
        print("valid")
    else:
        print("invalid")
        
        
        
import re

reg = r'[456]+(\d{15}|\d{3}-(\d{4}-?){3})'

while True:
    a = input().strip()
    if not a:
        break
    chk = re.match(reg,a)
    rep = re.search(r'(\d)\1{3,}',a.replace('-',''))
    if chk and not rep:
        print ("Valid")
    else:
        print ("Invalid")

