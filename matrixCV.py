rows = int(input('Nhap so hang i:'))
columns = int(input('Nhap so cot j:'))

matrix = []
for i in range(rows):
    row = []
    print('Nhap dong thu', i + 1, ':')
    for j in range(columns):
        x = int(input())
        row.append(x)
    
    matrix.append(row)

matrixCV = []
for i in range(columns):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])

    matrixCV.append(row)

print(matrixCV)