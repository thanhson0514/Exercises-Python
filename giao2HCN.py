from math import *

xA = int(input('Nhap xA:'))
yA = int(input('Nhap yA:'))
xB = int(input('Nhap xB:'))
yB = int(input('Nhap yB:'))
xC = int(input('Nhap xC:'))
yC = int(input('Nhap yC:'))
xD = int(input('Nhap xD:'))
yD = int(input('Nhap yD:'))

x_min = max(xA, xC)
x_max = min(xB, xD)
y_min = max(yA, yC)
y_max = min(yB, yD)

if x_min > x_max or y_min > y_max:
    print('Khong ton tai 2 HCN giao nhau.')
elif x_min == x_max or y_min == y_max:
    print('2 HCN trung nhau')
else:
    x = x_max - x_min
    y = y_max - y_min
    print('Dien tich HCN giao nhau la:', x*y)