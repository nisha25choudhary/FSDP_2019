a = '07:05:45AM'
b = a.split(':')
pm = b[2][2:]
if pm == 'PM':
     c = int(b[0])+12
     print(c,':',b[1],':',b[2][:-2])
else:
    x = [b[0],':',b[1],':',b[2][:-2]]
    print(x.split(','))  
