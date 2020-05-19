n = int(input("Nhap N:"))
print('Nhap',n, 'so:')

a = []

for i in range(n):
    x = int(input())
    a.append(x)

L = []

for i in range(n):
    L.append(0)

L[0] = a[0]
L[1] = max(a[0], a[1])

for i in range(2, n):
    x = max(a[i-2], 0)
    L[i] = max(L[i-1], a[i] + x)

print("Tong gia tri lon nhat:", L[n-1])
