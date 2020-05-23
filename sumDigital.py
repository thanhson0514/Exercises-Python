n1 = input('Nhap so thu 1:')
n2 = input('Nhap so thu 2:')

set1 = set(n1)
set2 = set(n2)

set3 = set1 & set2

total = 0
for i in set3:
    total += int(i)

print(total)