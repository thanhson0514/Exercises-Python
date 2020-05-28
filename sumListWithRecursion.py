n = int(input('Nhap n:'))

print('Nhap cac phan tu:')
List = [int(input()) for i in range(n)]
print(List)
total = 0
def sumList(n):
    if n == 1: return List[0]
    else: return List[n-1] + sumList(n-1)

print('Total:',sumList(len(List)))