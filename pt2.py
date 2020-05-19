from math import *

a = float(input('Nhap a:'))
b = float(input('Nhap b:'))
c = float(input('Nhap c:'))

if a == 0:
    if b == 0 and c != 0:
        print('Phuong trinh VN')
    elif b == 0 and c == 0:
        print('Phuong trinh co VSN')
    else:
        x = -c/b
        print('Nghiem pt la:', x)
elif a != 0:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print('Phuong trinh VN')
    elif de
if a < b and c < d:
    max_num = max(a, c)
    min_num = min(b, d)
    num = min_num - max_num + 1lta == 0:
        print('Phuong trinh co nghiem kep:', -b/(2*a))
    else:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        print('Phuong trinh co 2 nghiem phan biet:', x1, x2)
