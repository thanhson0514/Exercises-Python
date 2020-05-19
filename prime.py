from math import *

n = int(input('Nhap n:'))

if n <= 1:
    print(n, 'khong phai la so nguyen to.')
elif n == 2:
    print(n, 'la so nguyen to.')
else:
    isPrime = False
    for i in range(2, n):
        if n%i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    
    if isPrime:
        print(n, 'la so nguyen to.')
    else:
        print(n, 'khong la so nguyen to.')