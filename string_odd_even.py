'''
Given a string,S ,of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line(see the Sample below for more detail).
'''
n = int(input('number of string'))
ls = []
for i in range(n):
    s = input('string:')
    ls.append(s)
for  i in ls: 
    for j in range(0,len(i),2):
        print(i[j],end='')
    print(end=' ')
    for j in range(1,len(i),2):
        print(i[j],end='')
    print()
