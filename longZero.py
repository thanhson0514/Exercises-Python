from random import *

n = int(input('Nhap so phan tu:'))

List = []

for i in range(n):
    rd = randint(0,1)
    List.append(rd)

count = 0
result = []

print(List)

for i in List:
    if i == 0:
        count += 1
    else:
        result.append(count)
        count = 0

print(max(result))