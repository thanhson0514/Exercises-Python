dictionary = {}
n = int(input('Nhap so hoc sinh duoc thong ke:'))
for i in range(n):
    print('Ten ban thu', i+1, ':')
    name = input()
    point = -1
    while point < 0 or point > 10:
        print('Nhap diem cua',name,':')
        point = float(input())
    dictionary[name] = point

print(dictionary)