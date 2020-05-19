string = input('Nhap chuoi ki tu:')

st = ''

for i in range(len(string)):
    if '0' <= string[i] <= '9':
        st += '+' + string[i]

print(eval(st))