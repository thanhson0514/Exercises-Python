n = int(input('Nhap so khe:'))

print('Nhap so', n  + 1,'ngan:')
h = []

for i in range(n+1):
    x = int(input())
    h.append(x)

s = 0

for i in range(1, n+1):
    L = max(h[:i])
    R = max(h[i:])
    s += min(L,R)

print('Luong nuoc chua duoc la:', s)
