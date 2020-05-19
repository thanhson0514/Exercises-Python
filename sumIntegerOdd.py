listInt = list(input('Nhap chuoi ki tu khong khoang cach:'))

Sum = 0

for i in listInt:
    if int(i)%2 != 0:
        Sum += int(i)

print(Sum)

'''
*c2:
    listSum = []
    for i in listInt:
        if i%2 != 0:
            listSum.append(int(i)) 

    print(sum(listSum))
'''