string = input('Nhap chuoi ki tu:')

new_str = ''
string = string + '0'
a = 1

for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        a += 1
    elif a == 1:
        new_str += string[i]
    else:
        new_str += string[i] + str(a)
        a = 1

print('Ket qua:', new_str)

'''
    aaabbbbbdcc
    a3b
'''