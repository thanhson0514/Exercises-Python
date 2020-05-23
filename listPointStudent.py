n = int(input('Tong so hoc sinh tham gia thi hoc sinh gioi:'))

a = b = c = 0

while (a > n and b > n and c > n) or (a <= 0 and b <= 0 and c <= 0):
    a = int(input('So hoc sinh thi mon Toan:'))
    b = int(input('So hoc sinh thi mon Ly:'))
    c = int(input('So hoc sinh thi mon Hoa:'))
    if (a > n and b > n and c > n) or (a <= 0 and b <= 0 and c <= 0):
        print('Nhap lai. So cac hoc sinh tham gia cac mon khong vuot qua', n ,'hoac nho hon 0')

print('Nhap cac hoc sinh tham gia mon Toan:')
listA = {int(input()) for i in range(a)}
print('Nhap cac hoc sinh tham gia mon Ly:')
listB = {int(input()) for i in range(b)}
print('Nhap cac hoc sinh tham gia mon Hoa:')
listC = {int(input()) for i in range(c)}

print('Thi mot mon:')
print('Toan:', listA - (listB | listC))
print('Ly:', listB - (listA | listC))
print('Hoa:', listC - (listA | listB))

TLH = listA & listB & listC
print('Thi hai mon:')
print('Toan, Ly:', (listA & listB) - TLH)
print('Ly, Hoa:', (listB & listC) - TLH)
print('Toan, Hoa:', (listA & listC) - TLH)

print('thi ba mon:', TLH)