f = open('data/Data.txt', 'r')
list_line = f.readlines()
f.close()
f_latinh = open('data/Latinh.txt', 'a')
f_number = open('data/Number.txt', 'a')

for st in list_line:
    string = ''
    number = ''
    for i in st:
        if '0' <= i <= '9':
            number += i
        elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            string += i

    if string != '': f_latinh.writelines(string + '\n')
    if number != '': f_number.writelines(number + '\n')

f_latinh.close()
f_number.close()