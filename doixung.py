s1 = input('Nhap chuoi ki tu:')

s2 = s1[::-1]

if s1 == s2:
    print('Chuoi', s1, 'doi xung')
else:
    print('Chuoi', s1, 'khong doi xung')