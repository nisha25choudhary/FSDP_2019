# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:46:11 2019

@author: Lenovo
"""

"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same secret
 code name to multiple secret agents. 
Rewrite the above code using map and lambda.
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
       names[i] = random.choice(code_names)

print (names)
 
"""
rand = lambda names:random.choice(code_names)
print(rand(names))"""


names = ['Mary', 'Isla', 'Sam']
result = map(lambda names:random.choice(code_names) , names)
print(list(result))


def ran(names):

    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
    names = random.choice(code_names)

    return names

names = ['Mary', 'Isla', 'Sam']
result = map(ran , names)
print(list(result))




import random

names = ['Mary', 'Isla', 'Sam']

secret_names = list(map(lambda x: random.choice(['Mr. Pink','Mr. Orange','Mr. Blonde']),names))
