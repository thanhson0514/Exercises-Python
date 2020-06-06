a = int(input('Nhap a:'))
n = int(input('Nhap n:'))

# c1:
# def recursion(a,n):
#     if n == 1: return a
#     else: return a*recursion(n-1)

# print(recursion(a,n))

# C2:
def recursion(a,n):
    if n == 1: return a
    else:
        x = recursion(a, n//2)
        if n%2 == 0: return x*x
        else: return x*x*a

print(recursion(a, n))
