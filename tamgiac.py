a = int(input('Nhap a:'))
b = int(input('Nhap b:'))
c = int(input('Nhap c:'))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b+c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print('La tam giac vuong')
        elif a == b == c:
            print('La tam giac deu')
        else:
            print('La tam giac thuong')
    else:
        print('Khong phai la tam giac.')
else:
    print('Canh khong la so am.')