string = input('Nhap chuoi ki tu:')

new_string = ''

for i in range(len(string) - 1):
    if '0' <= string[i+1] <= '9':
        new_string += string[i]*int(string[i+1])
    else:
        if string[i] >= '9' or string[i] <= '0': 
            new_string += string[i]

print(new_string)