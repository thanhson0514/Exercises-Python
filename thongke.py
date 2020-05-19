from random import *

n = int(input('Nhap n:'))

List = []

for i in range(n):
    rd = randint(0,10e6)
    List.append(rd)

for i in List:
    count = List.count(i)
    print('Phan tu thu', i, 'xuat hien', count, 'lan')