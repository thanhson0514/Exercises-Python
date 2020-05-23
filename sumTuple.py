n = int(input('Nhap n:'))

tuple1 = ()

for i in range(1, n+1):
    tuple1 += (i,)

even = 0
odd = 0

for i in tuple1:
    if i%2 == 0:
        even += i
    else:
        odd += i

print('Tong so chan:', even)
print('Tong so le:', odd)
