string = input('Nhap chuoi ki tu:')

st = ''
string = string.lower()

for i in range(len(string)):
    if 'a' <= string[i] <= 'z':
        st += string[i]
    elif string[i].isspace():
        print(st)
        st = ''

print(st)