# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:20:19 2019

@author: Lenovo
"""

import re

with open("simpsons_phone_book.txt","r") as sim:
    read_line = sim.read()
    #res = re.findall('Neu',read_line)
    #print(res)
    result = re.findall(r"J.*Neu.*",read_line)
    print(result)
    
    
import re

fh = open("data/simpsons_phone_book.txt")
for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
fh.close()


