string = input('Nhap chuoi ki tu:')

str1 = ''
str2 = ''

for i in range(len(string)):
    if '0' <= string[i] <= '9':
        str1 += string[i]
    else:
        str2 += string[i]

print('Chuoi so:', str1)
print('Chuoi ki tu:', str2)