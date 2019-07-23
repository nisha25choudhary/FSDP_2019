#!/bin/python3
#Bubble sorting
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def bubble(a):
    swap =0
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap += 1
    return swap
print('Array is sorted in',bubble(a),'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])
