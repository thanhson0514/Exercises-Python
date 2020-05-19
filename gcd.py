# Don't use math library

a = int(input('Nhap a:'))
b = int(input('Nhap b:'))

min_num = 0
max_num = 0
ucln = 0

if a > b:
    max_num = a
    min_num = b
else:
    max_num = b
    min_num = a

for i in range(1, max_num + 1):
    if min_num%i == 0 and max_num%i == 0:
        ucln = i

bcnn = (a*b)/ucln

print('UCLN:', ucln)
print('BCNN:', bcnn)