#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appls= []
    orgls = []
    appc,orgc = 0,0
    for i in apples:
        ar = a+i
        appls.append(ar)
    for i in oranges:
        org = b+i
        orgls.append(org)
    for i in appls:
        if i >= s and i <= t:
            appc += 1
    for i in orgls:
        if i >= s and i <= t:
            orgc += 1
    print(appc)
    print(orgc)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)





'''
    Apple and Orange
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below,
the red region denotes his house, where is the start point, and is the endpoint. The apple tree is to the
left of his house, and the orange tree is to its right. You can assume the trees are located on a single
point, where the apple tree is at point , and the orange tree is at point .
When a fruit falls from its tree, it lands units of distance from its tree of origin along the -axis. A
negative value of means the fruit fell units to the tree's left, and a positive value of means it falls
units to the tree's right.
Complete the function countApplesAndOranges ,
where,
Starting point of Sam's house location.
Ending location of Sam's house location.
Location of the Apple tree.
Location of the Orange tree.
Number of apples that fell from the tree.
Distance at which each apple falls from the tree.
Number of oranges that fell from the tree.
Distance at which each orange falls from the tree.
Given the value of for apples and oranges, can you determine how many apples and oranges will
fall on Sam's house (i.e., in the inclusive range )? Print the number of apples that fall on Sam's house
as your first line of output, then print the number of oranges that fall on Sam's house as your second line
of output.
Input Format
The first line contains two space-separated integers denoting the respective values of and .
The second line contains two space-separated integers denoting the respective values of and .
The third line contains two space-separated integers denoting the respective values of and .
The fourth line contains space-separated integers denoting the respective distances that each apple
falls from point .
The fifth line contains space-separated integers denoting the respective distances that each orange falls
from point .
Constraints
Output Format
Print two lines of output:
1. On the first line, print the number of apples that fall on Sam's house.
2. On the second line, print the number of oranges that fall on Sam's house.
Sample Input 0
7 11
5 15
3 2
-2 2 1
5 -6
Sample Output 0
1
1
Explanation 0
The first apple falls at position .
The second apple falls at position .
The third apple falls at position .
The first orange falls at position .
The second orange falls at position .
Only one fruit (the second apple) falls within the region between and , so we print as our first line of
output.
Only the second orange falls within the region between and , so we print as our second line of
output.
''
