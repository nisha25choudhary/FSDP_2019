# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:05:18 2019

@author: Lenovo
"""
"""
  Problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)"""

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



def hash_n(names):
    names = hash(names)
    return names
#print(hash_n(names))

names = ['Mary', 'Isla', 'Sam']
res = map(hash_n,names)
print(list(res))




names = ['Mary', 'Isla', 'Sam']

secret_names = list(map(hash, names))
