# initial the first list
n1 = int(input('Nhap so phan tu danh sach thu nhat:'))
list1 = []

print('Nhap danh sach thu nhat:')
for i in range(n1):
    x = int(input())
    list1.append(x)

# initial the second list
n2 = int(input('Nhap so phan tu danh sach thu hai:'))
list2 = []

print('Nhap danh sach thu nhat:')
for i in range(n2):
    x = input()
    list1.append(x)

list1.sort()
list2.sort()

list1.extend(list2)
result = sorted(list1)

print(result)