n = int(input('Nhap n:'))

isRight = False

for i in range(0, n):
    for j in range(0, n):
        if (2**i)*(3**j) == n or (2**j)*(3**i) == n:
            isRight = True
            break
        else:
            isRight = False

    if isRight: break


if isRight:
    print(n, 'la luy thua 2 - 3.')
else:
    print(n, 'khong la luy thua 2 - 3.')