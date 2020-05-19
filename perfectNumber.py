n = int(input('Nhap n:'))

Sum = 0 

for i in range(1, n+1):
    if n%i == 0:
        Sum += i

if Sum == n*2:
    print(n, 'la so hoan hao.')
else:
    print(n,'khong la so hoan hao.')