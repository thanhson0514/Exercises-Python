m = int(input('Nhap so hang ma tran A:'))
nA = int(input('Nhap so cot ma tran A:'))
nB = int(input('Nhap so hang ma tran B:'))
k = int(input('Nhap so cot ma tran B:'))

if nA != nB:
    print('Khong the nhan ma tran. So cot ma tran A phai bang so hang ma tran B.')
else:
    print('---------------------------')
    print('Ma tran A')
    matrixA = []
    for i in range(m):
        row = []
        print('Nhap hang thu', i+1,':')
        for j in range(nA):
            x = int(input())
            row.append(x)

        matrixA.append(row)

    print('---------------------------')
    print('Ma tran B')
    matrixB = []
    for i in range(nB):
        row = []
        print('Nhap hang thu', i+1,':')
        for j in range(k):
            x = int(input())
            row.append(x)

        matrixB.append(row)

    mutiply = 1

    matrixC = []

    for i in range(m):
        row = []
        for j in range(k):
            c = 0
            for t in range(nA):
                c += matrixA[i][t] * matrixB[t][j]
            
            row.append(c)

        matrixC.append(row)
    print(matrixC)