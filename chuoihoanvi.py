string1 = input('Nhap chuoi ki tu 1:')
string2 = input('Nhap chuoi ki tu 2:')

string1 = ''.join(sorted(string1))
string2 = ''.join(sorted(string2))

if string1 == string2:
    print('La chuoi hoan vi.')
else:
    print('Khong la chuoi hoan vi.')