a = int(input('Nhap a:'))
n = int(input('Nhap n:'))

def recursion(n):
    if n == 1: return a
    else: return a*recursion(n-1)

print(recursion(n))