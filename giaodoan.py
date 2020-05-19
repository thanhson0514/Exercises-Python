from math import *

print('Nhap a,b trong doan [a,b] thoa man a < b va doan [c,d] thoa man c < d.')
a = int(input('Nhap a:'))
b = int(input('Nhap b:'))
c = int(input('Nhap c:'))
d = int(input('Nhap d:'))

'''
    [a, b] - [c, d]
    [3, 6] - [1, 3]
'''

if a < b and c < d:
    max_num = max(a, c)
    min_num = min(b, d)
    
    if max_num > min_num: print('Khong co so nao thoa man trong doan [a,b] va [c,d].')
    else:
        num = min_num - max_num + 1
        print('Co', num,'Trong doan [',max_num,',', min_num,']')
else: 
    print('Input khong thoa man')